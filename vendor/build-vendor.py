#!/usr/bin/env python3
"""vendor/ 재생성 스크립트.

이 폴더의 산출물은 전부 여기서 다시 만들 수 있다. 파일을 손으로 고치지 말고
버전 상수만 바꾼 뒤 다시 돌릴 것.

필요한 것 (fontTools는 노드 프로젝트에 안 들어가므로 venv를 따로 쓴다):

    python3 -m venv .venv
    ./.venv/bin/pip install fonttools brotli
    ./.venv/bin/python build-vendor.py

.venv 는 산출물이 아니므로 커밋하지 않는다.
"""

import re
import subprocess
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

MERMAID = "https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"

# lib.bundle.js 로 이어 붙일 것들. 순서가 의미를 갖는다 — autotable 은 jspdf 를 패치하므로
# 반드시 그 뒤에 와야 한다. index.html 의 CDN 폴백 목록도 이 순서/주소와 맞춰야 한다.
LIBS = [
    ("XLSX",      "https://cdn.sheetjs.com/xlsx-0.20.3/package/dist/xlsx.full.min.js"),
    ("LZString",  "https://cdnjs.cloudflare.com/ajax/libs/lz-string/1.5.0/lz-string.min.js"),
    ("jsPDF",     "https://cdnjs.cloudflare.com/ajax/libs/jspdf/3.0.3/jspdf.umd.min.js"),
    ("autoTable", "https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/5.0.2/jspdf.plugin.autotable.min.js"),
    ("PptxGenJS", "https://cdn.jsdelivr.net/gh/gitbrent/PptxGenJS@3.12.0/dist/pptxgen.bundle.js"),
]

# jsPDF 는 woff2 를 못 읽어서 PDF 한글용으로는 TTF 원본이 따로 필요하다.
PDF_TTF = "https://cdn.jsdelivr.net/npm/pretendard@1.3.9/dist/public/static/alternative/Pretendard-Regular.ttf"

PRETENDARD_TTF = "https://cdn.jsdelivr.net/npm/pretendard@1.3.9/dist/public/variable/PretendardVariable.ttf"
JBM_WOFF2 = "https://cdn.jsdelivr.net/npm/@fontsource-variable/jetbrains-mono@5/files/jetbrains-mono-latin-wght-normal.woff2"
OUTFIT_WOFF2 = "https://cdn.jsdelivr.net/npm/@fontsource-variable/outfit@5/files/outfit-latin-wght-normal.woff2"

LICENSES = [
    ("Pretendard 1.3.9", "https://raw.githubusercontent.com/orioncactus/pretendard/main/LICENSE"),
    ("JetBrains Mono",   "https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/OFL.txt"),
    ("Outfit",           "https://raw.githubusercontent.com/Outfitio/Outfit-Fonts/main/OFL.txt"),
]

# 한글을 뺀 나머지 — 라틴, 구두점, 통화, 화살표, 괘선, 도형/이모지 계열, 전각.
# 다이어그램 라벨에 실제로 나오는 범위만 남긴 것이다.
BASE_RANGES = ("U+0020-007E,U+00A0-00FF,U+0100-017F,U+2000-206F,U+20A9,U+20AC,"
               "U+2190-2193,U+2500-257F,U+25A0-25FF,U+2600-26FF,U+3000-303F,"
               "U+1100-11FF,U+3131-318E,U+FF01-FF5E,U+FFE0-FFE6")

HANGUL_FIRST, HANGUL_LAST = 0xAC00, 0xD7A3


def fetch(url: str) -> bytes:
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA)).read()


def to_ranges(codepoints) -> str:
    """정렬된 코드포인트 목록을 CSS unicode-range 문자열로 압축한다."""
    out, start, prev = [], None, None
    for cp in codepoints:
        if start is None:
            start = prev = cp
        elif cp == prev + 1:
            prev = cp
        else:
            out.append(f"U+{start:04X}" if start == prev else f"U+{start:04X}-{prev:04X}")
            start = prev = cp
    if start is not None:
        out.append(f"U+{start:04X}" if start == prev else f"U+{start:04X}-{prev:04X}")
    return ",".join(out)


def ks_x_1001_syllables():
    """KS X 1001 완성형 한글 2,350자. EUC-KR 2바이트 중 선행 바이트가 0xB0-0xC8 인 것."""
    out = []
    for cp in range(HANGUL_FIRST, HANGUL_LAST + 1):
        try:
            b = chr(cp).encode("euc-kr")
        except UnicodeEncodeError:
            continue
        if len(b) == 2 and 0xB0 <= b[0] <= 0xC8:
            out.append(cp)
    return out


def subset(src: Path, dest: Path, unicodes: str):
    subprocess.run(
        [sys.executable, "-m", "fontTools.subset", str(src),
         f"--output-file={dest}", "--flavor=woff2", f"--unicodes={unicodes}",
         "--layout-features=*", "--no-hinting", "--drop-tables+=DSIG"],
        check=True, capture_output=True,
    )


def weight_axis(path: Path):
    """가변 폰트의 wght 축 범위를 읽어 @font-face 의 font-weight 에 그대로 쓴다."""
    from fontTools.ttLib import TTFont
    with TTFont(path, lazy=True) as f:
        for axis in f["fvar"].axes:
            if axis.axisTag == "wght":
                return int(axis.minValue), int(axis.maxValue)
    return 400, 400


def face(family, path: Path, unicode_range=None):
    lo, hi = weight_axis(path) if path.suffix == ".woff2" else (400, 400)
    rng = f"\n  unicode-range: {unicode_range};" if unicode_range else ""
    return (f"@font-face {{\n"
            f"  font-family: '{family}';\n"
            f"  font-style: normal;\n"
            f"  font-display: swap;\n"
            f"  font-weight: {lo} {hi};\n"
            f"  src: url({path.name}) format('woff2');{rng}\n"
            f"}}")


def main():
    work = HERE / ".build"
    work.mkdir(exist_ok=True)

    print("libs → lib.bundle.js")
    parts = []
    for name, url in LIBS:
        raw = fetch(url).decode("utf-8")
        print(f"  {name:10s} {len(raw)//1024:5d} KB")
        # 앞 파일이 세미콜론 없이 끝나도 다음 파일과 붙지 않도록 사이에 ';' 를 끼운다.
        parts.append(f"/* ── {name} — {url} ── */\n{raw}\n;\n")
    (HERE / "lib.bundle.js").write_text("".join(parts), encoding="utf-8")

    print("mermaid.min.js / Pretendard-Regular.ttf (원본 그대로)")
    (HERE / "mermaid.min.js").write_bytes(fetch(MERMAID))
    (HERE / "Pretendard-Regular.ttf").write_bytes(fetch(PDF_TTF))

    print("fonts")
    src = work / "PretendardVariable.ttf"
    src.write_bytes(fetch(PRETENDARD_TTF))

    ks = ks_x_1001_syllables()
    rest = [cp for cp in range(HANGUL_FIRST, HANGUL_LAST + 1) if cp not in set(ks)]
    ks_ranges, rest_ranges = to_ranges(ks), to_ranges(rest)
    print(f"  KS X 1001 {len(ks)}자 / 그 외 한글 {len(rest)}자")

    # 겹치지 않는 두 구간으로 자른다. 겹치게 두면 어느 face 가 이기는지가 CSS 선언
    # 순서 규칙에 걸리는데, 그 규칙에 1.3 MB 를 걸 이유가 없다.
    subset(src, HERE / "pretendard-common.woff2", f"{BASE_RANGES},{ks_ranges}")
    subset(src, HERE / "pretendard-rest.woff2", rest_ranges)
    (HERE / "jetbrains-mono.woff2").write_bytes(fetch(JBM_WOFF2))
    (HERE / "outfit.woff2").write_bytes(fetch(OUTFIT_WOFF2))

    css = [
        "/* 자동 생성 — build-vendor.py 로 다시 만든다. 직접 고치지 말 것.",
        " * 폰트 3종 모두 SIL OFL 1.1, 전문은 같은 폴더의 LICENSES.txt 에 있다.",
        " *",
        " * Pretendard 는 두 조각으로 잘라 뒀다. 상용 한글(KS X 1001 2,350자)은",
        " * pretendard-common 에, 나머지 8,822자는 pretendard-rest 에 들어간다.",
        " * 두 구간이 겹치지 않으므로 브라우저는 실제로 그리는 글자가 속한 쪽만 받아간다",
        " * — 흔한 한글만 쓰면 rest 는 아예 요청되지 않는다. */",
        "",
        face("Pretendard", HERE / "pretendard-common.woff2", f"{BASE_RANGES},{ks_ranges}"),
        "",
        face("Pretendard", HERE / "pretendard-rest.woff2", rest_ranges),
        "",
        face("JetBrains Mono", HERE / "jetbrains-mono.woff2"),
        "",
        face("Outfit", HERE / "outfit.woff2"),
        "",
    ]
    (HERE / "fonts.css").write_text("\n".join(css), encoding="utf-8")

    print("LICENSES.txt")
    chunks = []
    for name, url in LICENSES:
        bar = "=" * 70
        chunks.append(f"{bar}\n{name}\n{url}\n{bar}\n\n{fetch(url).decode('utf-8').strip()}\n")
    (HERE / "LICENSES.txt").write_text("\n\n".join(chunks), encoding="utf-8")

    for f in sorted(HERE.iterdir()):
        if f.is_file() and f.name not in ("build-vendor.py", "README.md"):
            print(f"  {f.stat().st_size/1024:8.0f} KB  {f.name}")


if __name__ == "__main__":
    main()
