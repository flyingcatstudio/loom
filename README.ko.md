<p align="right">
  <a href="README.md">English</a> · <strong>한국어</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Loom-Architecture%20Weaver-58a6ff?style=for-the-badge&labelColor=0d1117" alt="Loom" />
</p>

<h1 align="center">Loom</h1>

<p align="center">
  <strong>인프라의 흐름을 직조하는 k8s 아키텍처 에디터</strong><br/>
  베틀이 실을 엮어 천을 만들듯, Loom은 인프라 구성요소를 엮어 아키텍처를 만듭니다.
</p>

<p align="center">
  <a href="https://aiotool.net">🌐 바로 사용하기</a> &nbsp;·&nbsp;
  <a href="#-설치-방법">📦 설치</a> &nbsp;·&nbsp;
  <a href="#-사용-매뉴얼">📖 매뉴얼</a> &nbsp;·&nbsp;
  <a href="#-라이선스">📄 라이선스</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-AGPL--3.0-blue" alt="License" />
  <img src="https://img.shields.io/badge/version-2.0-green" alt="Version" />
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen" alt="Zero Dependencies" />
  <img src="https://img.shields.io/badge/install-not%20required-orange" alt="No Install" />
</p>

---

## 📋 개요

**Loom**은 MCU 드라마 <로키>의 **Temporal Loom(시간의 직조기)** 에서 영감을 받았습니다.

Kubernetes 인프라 아키텍처를 빠르게 설계하기 위한 **단일 HTML 파일** 기반 에디터입니다. 설치 없이 브라우저에서 바로 실행되며, 인터넷이 차단된 **보안망(에어갭 환경)에서도 즉시 사용** 가능합니다.

> **단일 파일 철학** — `index.html` 파일이 크지만, Loom은 의도적으로 모든 것을 하나의 파일에 담습니다. 빌드 도구, 의존성, 서버 없이 파일 하나만 열면 바로 사용할 수 있도록 **휴대성과 사용 편의성**을 최우선으로 합니다.

k8s 클러스터의 리소스(CPU, Memory, Disk, GPU) 사용량을 노드별로 설정하고 **실시간 대시보드**에서 한눈에 확인할 수 있습니다. AI 다이어그램 자동 생성은 Claude, OpenAI, Gemini뿐 아니라 **Ollama를 통한 로컬 LLM**도 지원하여 보안망에서도 AI 기능을 활용할 수 있습니다.

### 왜 Loom인가?

| 특징 | Loom | 기존 도구 |
|------|------|-----------|
| **설치** | 불필요 (HTML 파일 1개) | 설치/가입 필요 |
| **비용** | 무료 | 대부분 유료 |
| **보안망** | 즉시 사용 가능 | 인터넷 필요 |
| **k8s 리소스 관리** | 실시간 대시보드 내장 | 별도 도구 필요 |
| **AI 생성** | 로컬 LLM (Ollama) 지원 | 클라우드 API만 지원 |
| **내보내기** | JSON / Excel / PDF / PNG / k8s YAML / Terraform / Helm | 제한적 |

### 주요 기능

- **캔버스 기반 다이어그램 에디터** — 노드 생성, 연결, 그룹핑, 레이어 관리
- **레이어 표시/숨김 토글** — 눈 아이콘으로 레이어별 표시/숨김 전환; 숨긴 레이어는 캔버스, 선택, 리소스 계산에서 제외
- **120+ 클라우드 아이콘** — AWS, GCP, Azure, Kubernetes, 오픈소스 아이콘 내장
- **k8s 리소스 대시보드** — 클러스터 하드웨어 설정, 노드별 CPU/메모리/디스크/GPU 리소스 관리 (보이는 레이어만 집계)
- **인프라 완성도 체크** — 필수 구성요소 누락, 네트워크 연결, 리소스 초과 자동 감지
- **AI 다이어그램 생성** — 텍스트 설명으로 아키텍처 자동 생성 (Claude / OpenAI / Gemini / Ollama)
- **다양한 내보내기** — JSON, Excel (리소스 시트 포함), PDF (표지+다이어그램+상세표), PNG
- **IaC 코드 내보내기** — k8s YAML, Terraform (HCL), Helm Values를 노드별 또는 전체 인프라로 생성
- **연결선 Waypoint** — 연결선 경로를 꺾어서 세밀하게 제어
- **자동 레이아웃** — 노드 자동 배치
- **다크/라이트 테마** — 테마 전환 시 노드 텍스트 색상이 배경에 맞춰 자동 조정
- **세션 유지** — 브라우저 새로고침 시 위치, 줌, 레이어, k8s 설정 등 전체 상태 복원
- **한국어/영어 지원** — UI 전체 다국어 전환
- **Undo/Redo** — 전체 작업 이력 관리

---

## 🖼 스크린샷

### AI 프롬프트로 아키텍처 설계

AI에게 텍스트로 아키텍처를 설명하면 다이어그램을 자동 생성합니다.

<p align="center">
  <img src="sample/prompt_example.png" alt="AI Prompt Example" width="500" />
</p>

### 설계 결과 다이어그램

AI가 생성한 CI/CD 파이프라인 아키텍처 — 그룹으로 구성된 전체 흐름을 한눈에 확인할 수 있습니다.

<p align="center">
  <img src="sample/diagram_example.png" alt="Diagram Example" width="800" />
</p>

### k8s 클러스터 설정

워커 노드의 CPU, Memory, Disk, GPU 사양과 시스템 예약 리소스를 설정합니다. 총 할당 가능 리소스가 자동으로 계산됩니다.

<p align="center">
  <img src="sample/k8s_setting_example.png" alt="k8s Cluster Settings" width="500" />
</p>

### k8s 리소스 현황 대시보드

설정된 클러스터 리소스와 다이어그램 내 노드들의 리소스 요구사항을 비교하여 사용률과 상태를 실시간으로 보여줍니다.

<p align="center">
  <img src="sample/k8s_resource_example.png" alt="k8s Resource Dashboard" width="300" />
</p>

---

## 📦 설치 방법

### 방법 1: 온라인 사용 (설치 불필요)

**[https://aiotool.net](https://aiotool.net)** 에 접속하면 바로 사용할 수 있습니다.

### 방법 2: 로컬 파일 다운로드

```bash
# 저장소 클론
git clone https://github.com/flyingcatstudio/loom.git

# 브라우저에서 열기
open index.html
```

또는 `index.html` 파일 하나만 다운로드하여 브라우저에서 열면 됩니다.

> **보안망(에어갭) 환경**: HTML 파일을 USB 등으로 복사 후 브라우저에서 열면 됩니다. 외부 의존성 없이 동작합니다. (폰트만 CDN 사용 — 오프라인에서는 시스템 폰트로 대체됩니다)

### 방법 3: AI 기능 (Ollama 로컬 LLM — On-Premise)

보안망(에어갭) 환경에서 AI 기능을 사용하려면 Ollama와 모델을 **외부에서 미리 다운로드**하여 반입해야 합니다.

#### 1단계: 외부 인터넷 환경에서 준비

```bash
# Ollama 설치 패키지 다운로드
# macOS: https://ollama.com/download/Ollama-darwin.zip
# Linux: https://ollama.com/download/ollama-linux-amd64.tgz
# Windows: https://ollama.com/download/OllamaSetup.exe

# 모델 파일 다운로드 (Ollama 설치 후)
ollama pull llama3
```

모델 파일 위치:
- **macOS / Linux**: `~/.ollama/models/`
- **Windows**: `%USERPROFILE%\.ollama\models\`

#### 2단계: 보안망으로 반입

다운로드한 파일들을 USB 등의 매체로 보안망 PC에 복사합니다:

1. **Ollama 설치 패키지** (zip / tgz / exe)
2. **models 폴더 전체** (`~/.ollama/models/`)

#### 3단계: 보안망에서 설치 및 실행

```bash
# 1. Ollama 설치 패키지 실행/압축 해제하여 설치

# 2. 모델 파일을 ~/.ollama/models/ 에 복사
cp -r /USB경로/models/ ~/.ollama/models/

# 3. Ollama 서버 시작
ollama serve
```

Loom의 **✦ AI 생성** 패널에서 서비스를 `Ollama`로 선택하면 로컬 LLM으로 다이어그램을 생성할 수 있습니다.

---

## 📖 사용 매뉴얼

### 기본 조작

| 동작 | 방법 |
|------|------|
| **노드 생성** | 캔버스 빈 곳 더블클릭 / 왼쪽 팔레트에서 드래그 |
| **노드 이동** | 노드를 드래그 |
| **노드 크기 조정** | 선택 후 우하단 핸들 드래그 |
| **연결선 생성** | `C` 키 또는 연결 도구 선택 → 시작 노드 클릭 → 끝 노드 클릭 |
| **선택** | `V` 키 또는 선택 도구로 클릭 |
| **다중 선택** | `Shift+Click` 또는 빈 곳에서 드래그(마키) |
| **전체 선택** | `Ctrl+A` |
| **캔버스 이동** | `Space` 누른 채 드래그 / 마우스 휠 클릭 드래그 |
| **확대/축소** | 마우스 휠 스크롤 / 상단 +/−/100% 버튼 |
| **이름 변경** | 노드 더블클릭 |
| **삭제** | `Delete` 또는 `Backspace` |
| **실행 취소/다시 실행** | `Ctrl+Z` / `Ctrl+Y` |
| **복사/붙여넣기** | `Ctrl+C` / `Ctrl+V` |
| **잘라내기** | `Ctrl+X` |

### 연결선 편집

| 동작 | 방법 |
|------|------|
| **연결선 선택** | 연결선 클릭 |
| **연결 대상 변경** | 끝점 핸들(●)을 다른 노드로 드래그 |
| **끝점 위치 고정** | `Alt` + 끝점 핸들 드래그 (노드 테두리 위 고정) |
| **끝점 고정 해제** | 끝점 핸들 더블클릭 |
| **경로 꺾기 (Waypoint)** | 연결선 선택 → 중간점(⊕) 드래그 |
| **꺾인점 삭제** | 꺾인점(●) 더블클릭 |
| **연결 스타일** | 우측 패널에서 실선/점선/양방향 선택 |

### k8s 리소스 관리

#### 1. 클러스터 설정

상단 **☸ k8s 리소스** 버튼을 클릭하여 클러스터를 설정합니다:

- **하드웨어 탭**: 워커 노드 수, 노드당 CPU/Memory/Disk, GPU 노드, 시스템 예약 리소스
- **스케줄링 탭**: 네임스페이스, Taint, 노드 라벨 설정

<p align="center">
  <img src="sample/k8s_setting_example.png" alt="k8s Cluster Settings" width="450" />
</p>

#### 2. 노드별 리소스 할당

인프라 노드 (Server, Database 등)를 선택하면 우측 패널에 나타나는 항목:

- **📦 스케줄링**: 네임스페이스 배정, Toleration, NodeSelector
- **☸ 리소스**: Min/Max CPU, Memory, Disk, GPU, Replicas

#### 3. 리소스 대시보드

우측 하단 **☸ k8s Resource** 섹션에서 실시간 확인:

- CPU/Memory/Disk/GPU 사용률 바 (Min~Max 범위 표시)
- 상태 뱃지: `OK` `Warning` `Critical` `Over`
- 캔버스 위 각 노드에도 CPU 미니바 표시

<p align="center">
  <img src="sample/k8s_resource_example.png" alt="k8s Resource Dashboard" width="250" />
</p>

#### 4. 인프라 완성도 체크

상단 **✅ 인프라 체크** 버튼으로 아키텍처 검증:

- 필수 인프라 구성요소 존재 여부
- 네트워크 연결 상태
- 미사용 리소스 감지
- 리소스 초과 경고

### AI 다이어그램 생성

상단 **✦ AI 생성** 버튼으로 AI 패널을 엽니다.

<p align="center">
  <img src="sample/prompt_example.png" alt="AI Prompt" width="450" />
</p>

#### 지원 AI 서비스

| 서비스 | 모델 | 요구사항 |
|--------|------|----------|
| **Ollama** (로컬) | llama3, codellama, mistral 등 | Ollama 설치 |
| **Claude** | Sonnet, Opus, Haiku | API 키 |
| **OpenAI** | GPT-4, GPT-4 Turbo, GPT-3.5 | API 키 |
| **Gemini** | Gemini | API 키 |

#### 사용법

1. AI 패널에서 서비스 선택 및 설정
2. 생성 모드 선택:
   - **새로 생성**: 처음부터 다이어그램 생성
   - **기존에 추가**: 현재 다이어그램에 추가
   - **현재 수정**: 현재 다이어그램 수정
3. 텍스트로 아키텍처 설명 입력 (예: *"k8s 마이크로서비스: API Gateway, 서비스 3개, PostgreSQL, Redis, Kafka"*)
4. `Ctrl+Enter`로 전송

<p align="center">
  <img src="sample/diagram_example.png" alt="Generated Diagram" width="800" />
</p>

### 내보내기 / 가져오기

상단 **Import/Export** 드롭다운 메뉴:

| 형식 | 설명 |
|------|------|
| **JSON** 💾 | 전체 다이어그램 저장/불러오기 (k8s 설정 포함) |
| **Excel** 📊 | 노드 목록 + k8s 리소스 요약 시트 |
| **PDF** 📄 | 표지 + 다이어그램 + 노드 상세표 + 리소스 요약 |
| **PNG** 📷 | 다이어그램 이미지 캡처 |
| **k8s YAML** ☸ | Deployment / StatefulSet / Service / PVC 매니페스트 |
| **Terraform** ⛅ | HCL 형식의 kubernetes provider 리소스 코드 |
| **Helm Values** ⎈ | values.yaml 형식의 서비스별 설정 |

#### IaC 코드 내보내기

설계한 아키텍처를 실제 배포 가능한 IaC(Infrastructure as Code) 코드로 내보낼 수 있습니다.

**전체 내보내기**: Export 드롭다운 메뉴에서 k8s YAML / Terraform / Helm Values 선택

**노드별 내보내기**: 우측 k8s 리소스 대시보드에서 각 노드의 `[Y]` `[T]` `[H]` 미니 버튼 클릭

| 노드 타입 | k8s 리소스 | 서비스 타입 |
|-----------|-----------|------------|
| Server, Service, Queue | Deployment + Service(ClusterIP) | ClusterIP |
| Gateway | Deployment + Service(LoadBalancer) | LoadBalancer |
| Database | StatefulSet + Service(headless) + PVC | ClusterIP (headless) |
| Storage | PersistentVolumeClaim | — |

생성된 코드에는 노드에 설정된 리소스 요구사항(CPU/Memory/Disk/GPU), 레플리카 수, Toleration, NodeSelector가 모두 반영됩니다.

---

## 🗺 Roadmap

추후 업데이트 예정인 기능들입니다. 기여와 제안을 환영합니다!

- [x] 다크/라이트 테마 전환
- [x] 한국어/영어 UI 전환
- [x] Helm Values / k8s YAML 자동 생성
- [x] Terraform 코드 내보내기
- [ ] 템플릿 공유하기

---

## 📄 라이선스

이 프로젝트는 [**GNU Affero General Public License v3.0 (AGPL-3.0)**](LICENSE) 하에 배포됩니다.

**상업적 목적으로 재판매하는 것을 제외하면** 자유롭게 사용할 수 있습니다. 단, 수정한 코드는 반드시 동일한 라이선스로 소스 코드를 공개해야 합니다.

> 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

## 🏢 제작

<p align="center">
  <strong>FCStudio</strong><br/>
  <a href="https://aiotool.net">aiotool.net</a> · <a href="https://fcs-game.com">fcs-game.com</a>
</p>

---

<p align="center">
  <sub>Made with 🐱 by <strong>FCStudio</strong></sub>
</p>