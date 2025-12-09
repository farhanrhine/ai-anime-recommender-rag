# 🎌 AI Anime Recommender System

A production-grade **RAG-powered Anime Recommendation System** built with **LangChain**, **ChromaDB**, **Groq LLM (Llama 3.1)**, deployed on **Google Kubernetes Engine (GKE) Autopilot** with **GitHub Actions CI/CD**.

[![Docker](https://img.shields.io/badge/Docker-Hub-blue?logo=docker)](https://hub.docker.com/r/farhanrhine/anime-recommender-api)
[![GKE](https://img.shields.io/badge/GKE-Autopilot-4285F4?logo=google-cloud)](https://cloud.google.com/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-green)](https://langchain.com/)

---

## 📌 Overview

This project is an **AI-powered anime recommendation system** that uses **Retrieval-Augmented Generation (RAG)** to provide personalized anime recommendations. It combines:

- **Vector Search**: ChromaDB stores anime embeddings for semantic similarity search
- **LLM Reasoning**: Groq's Llama 3.1 generates natural language recommendations
- **Production Deployment**: GKE Autopilot with persistent storage for vector database
- **Observability**: LangSmith tracing for LLM pipeline monitoring

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           AI ANIME RECOMMENDER                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────────────────────┐ │
│   │   Streamlit  │───→│   FastAPI    │───→│     RAG Pipeline             │ │
│   │   Frontend   │    │   Backend    │    │  ┌────────────────────────┐  │ │
│   └──────────────┘    └──────────────┘    │  │ ChromaDB Vector Store  │  │ │
│                              │            │  └──────────┬─────────────┘  │ │
│                              │            │             ↓                │ │
│                              │            │  ┌────────────────────────┐  │ │
│                              │            │  │   HuggingFace Embed    │  │ │
│                              │            │  │ (all-MiniLM-L6-v2)     │  │ │
│                              │            │  └──────────┬─────────────┘  │ │
│                              │            │             ↓                │ │
│                              │            │  ┌────────────────────────┐  │ │
│                              │            │  │   Groq LLM (Llama 3.1) │  │ │
│                              │            │  └────────────────────────┘  │ │
│                              │            └──────────────────────────────┘ │
│                              ↓                                             │
│                    ┌──────────────────┐                                    │
│                    │   LangSmith      │                                    │
│                    │   Tracing        │                                    │
│                    └──────────────────┘                                    │
└─────────────────────────────────────────────────────────────────────────────┘

                    DEPLOYMENT: GKE Autopilot + Persistent Disk
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   GitHub Actions ──→ DockerHub ──→ GKE Autopilot                           │
│        CI/CD           Image         Cluster                                │
│                                         │                                   │
│                         ┌───────────────┼───────────────┐                  │
│                         │               │               │                  │
│                         ▼               ▼               ▼                  │
│                   ┌──────────┐   ┌──────────┐   ┌──────────────┐           │
│                   │ Pod with │   │ K8s      │   │ GCP          │           │
│                   │ FastAPI  │   │ Secrets  │   │ Persistent   │           │
│                   │ Container│   │          │   │ Disk (20GB)  │           │
│                   └──────────┘   └──────────┘   │ ChromaDB     │           │
│                                                 └──────────────┘           │
│                                         │                                   │
│                                         ▼                                   │
│                               ┌──────────────────┐                         │
│                               │   LoadBalancer   │                         │
│                               │   External IP    │                         │
│                               └──────────────────┘                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Features

- **🔍 Semantic Search**: Vector similarity search using ChromaDB + HuggingFace embeddings
- **🤖 LLM-Powered Recommendations**: Natural language responses via Groq Llama 3.1
- **⚡ Fast Cold Start**: Pre-built vector store loaded from persistent disk
- **🔐 Secure**: Kubernetes Secrets for API keys, no secrets in code
- **📊 Observable**: LangSmith tracing for full LLM pipeline visibility
- **🔄 CI/CD**: GitHub Actions auto-deploys to GKE on push
- **☸️ Cloud Native**: GKE Autopilot with auto-scaling and managed infrastructure

---

## 📦 Project Structure

```
ai_anime_recommender_system/
│
├── pyproject.toml              # UV package manager config & dependencies
├── uv.lock                     # Locked dependency versions
├── .env                        # Local secrets (not committed)
├── .gitignore                  # Ignored files/folders
├── README.md                   # This file
│
├── data/
│   ├── anime_with_synopsis.csv       # Raw anime dataset
│   └── anime_processed.csv           # Processed dataset for embeddings
│
├── chroma_db/                  # Vector store (generated, gitignored)
├── chroma_db.zip               # Zipped vector store for GCP disk upload
│
├── src/
│   └── recommender_system/
│       ├── __init__.py
│       │
│       ├── data_loader.py            # CSV loading & preprocessing
│       ├── vector_store.py           # ChromaDB operations
│       ├── recommender.py            # RAG chain logic
│       ├── prompt_template.py        # LLM prompt templates
│       │
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── logger.py             # Logging configuration
│       │   └── custom_exception.py   # Custom error handling
│       │
│       ├── config/
│       │   ├── __init__.py
│       │   └── settings.py           # Environment & model settings
│       │
│       ├── pipeline/
│       │   ├── __init__.py
│       │   ├── build_embedding_pipeline.py   # One-time embedding creation
│       │   └── recommend_pipeline.py         # Runtime recommendation pipeline
│       │
│       └── api/
│           ├── __init__.py
│           ├── fastapi_app.py        # FastAPI application
│           └── models.py             # Pydantic request/response models
│
├── app/
│   └── streamlit_app.py        # Streamlit frontend UI
│
├── docker/
│   └── Dockerfile              # Production Docker image (UV + FastAPI)
│
├── kubernetes/
│   ├── storageclass.yaml       # GKE storage class for persistent disk
│   ├── pv.yaml                 # PersistentVolume (GCP disk binding)
│   ├── pvc.yaml                # PersistentVolumeClaim
│   ├── secret.yaml             # Kubernetes secrets template
│   ├── deployment.yaml         # Pod deployment spec
│   └── service.yaml            # LoadBalancer service
│
└── .github/
    └── workflows/
        └── deploy-gke.yml      # GitHub Actions CI/CD workflow
```

---

## 🧩 Component Details

### 📁 **Core Modules** (`src/recommender_system/`)

| File                 | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| `data_loader.py`     | Loads and preprocesses anime CSV data                       |
| `vector_store.py`    | ChromaDB operations: build, persist, and load vector stores |
| `recommender.py`     | RAG pipeline using LangChain LCEL with Groq LLM             |
| `prompt_template.py` | Custom prompt templates for anime recommendations           |

### ⚙️ **Config & Utils**

| File                        | Description                                          |
| --------------------------- | ---------------------------------------------------- |
| `config/settings.py`        | Loads API keys from environment, defines model names |
| `utils/logger.py`           | Structured logging with timestamps                   |
| `utils/custom_exception.py` | Custom exception classes for clean error handling    |

### 🔄 **Pipelines**

| File                          | Description                                                   |
| ----------------------------- | ------------------------------------------------------------- |
| `build_embedding_pipeline.py` | **One-time**: Creates embeddings from CSV → ChromaDB          |
| `recommend_pipeline.py`       | **Runtime**: Loads vector store and generates recommendations |

### 🌐 **API Layer** (`src/recommender_system/api/`)

| Endpoint     | Method | Description                     |
| ------------ | ------ | ------------------------------- |
| `/`          | GET    | Health message (human-readable) |
| `/health`    | GET    | Health check (machine-readable) |
| `/recommend` | POST   | Get anime recommendations       |

---

## 🛠️ Tech Stack

| Category            | Technology                                   |
| ------------------- | -------------------------------------------- |
| **Language**        | Python 3.12                                  |
| **Package Manager** | UV (astral-sh)                               |
| **LLM**             | Groq Llama 3.1 8B Instant                    |
| **Embeddings**      | HuggingFace `all-MiniLM-L6-v2`               |
| **Vector Store**    | ChromaDB                                     |
| **Framework**       | LangChain + LangChain Community              |
| **API**             | FastAPI + Uvicorn                            |
| **Frontend**        | Streamlit                                    |
| **Container**       | Docker (UV base image)                       |
| **Orchestration**   | Kubernetes (GKE Autopilot)                   |
| **CI/CD**           | GitHub Actions                               |
| **Cloud**           | Google Cloud Platform (GKE, Persistent Disk) |
| **Observability**   | LangSmith Tracing                            |

---

## 🏃 Quick Start (Local Development)

### Prerequisites

- Python 3.12+
- [UV](https://github.com/astral-sh/uv) package manager
- API Keys: `GROQ_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`

### 1. Clone & Setup

```bash
git clone https://github.com/farhanrhine/Al-Anime-Recommender-System-using-Grafana-Cloud-Minikube-ChromaDB-Langchain-GCP.git
cd Al-Anime-Recommender-System
```

### 2. Create `.env` file

```env
GROQ_API_KEY=your_groq_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token

# Optional: LangSmith Tracing
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT=anime-recommender
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
```

### 3. Install Dependencies

```bash
uv sync
```

### 4. Build Embeddings (One-time)

```bash
uv run python src/recommender_system/pipeline/build_embedding_pipeline.py
```

### 5. Run FastAPI Server

```bash
uv run uvicorn recommender_system.api.fastapi_app:app --reload
```

### 6. (Optional) Run Streamlit Frontend

```bash
uv run streamlit run app/streamlit_app.py
```

---

## 🐳 Docker

### Build Image

```bash
docker build -f docker/Dockerfile -t anime-recommender-api .
```

### Run Container

```bash
docker run -d \
  -p 8000:8000 \
  -e GROQ_API_KEY=your_key \
  -e HUGGINGFACEHUB_API_TOKEN=your_token \
  -v /path/to/chroma_db:/app/chroma_db \
  anime-recommender-api
```

### DockerHub Image

```bash
docker pull farhanrhine/anime-recommender-api:latest
```

---

## ☸️ Kubernetes Deployment (GKE Autopilot)

### Architecture Overview

The deployment uses:

- **GKE Autopilot**: Managed Kubernetes with auto-scaling
- **Persistent Disk**: 20GB GCE disk (`ai-anime-chroma-disk`) with pre-loaded ChromaDB
- **LoadBalancer**: External IP for API access
- **Kubernetes Secrets**: Secure API key storage

### Kubernetes Manifests

| File                | Purpose                                                                           |
| ------------------- | --------------------------------------------------------------------------------- |
| `storageclass.yaml` | Defines `chroma-storage` class with GCE PD provisioner                            |
| `pv.yaml`           | Binds to `ai-anime-chroma-disk` GCP persistent disk                               |
| `pvc.yaml`          | Claims 20GB from the PV                                                           |
| `deployment.yaml`   | Deploys `farhanrhine/anime-recommender-api:latest` with secrets and volume mounts |
| `service.yaml`      | Exposes API via LoadBalancer on port 8000                                         |

### Secrets Required

Before deploying, create the Kubernetes secret:

```bash
kubectl create secret generic anime-secrets \
  --from-literal=GROQ_API_KEY=your_key \
  --from-literal=HUGGINGFACEHUB_API_TOKEN=your_token \
  --from-literal=LANGCHAIN_API_KEY=your_langsmith_key \
  --from-literal=LANGCHAIN_TRACING_V2=true \
  --from-literal=LANGCHAIN_ENDPOINT=https://api.smith.langchain.com \
  --from-literal=LANGCHAIN_PROJECT=anime-recommender
```

### Manual Deploy

```bash
kubectl apply -f kubernetes/storageclass.yaml
kubectl apply -f kubernetes/pv.yaml
kubectl apply -f kubernetes/pvc.yaml
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

### Get External IP

```bash
kubectl get svc anime-service
```

---

## 🔄 CI/CD: GitHub Actions → GKE Autopilot

### Workflow Overview

The GitHub Actions workflow (`.github/workflows/deploy-gke.yml`) automatically:

1. **Authenticates** to GCP using service account key
2. **Configures** kubectl for the GKE cluster
3. **Deploys** Kubernetes manifests from `kubernetes/` folder
4. **Creates/Updates** secrets from GitHub Secrets

### Required GitHub Secrets

| Secret Name           | Description                    |
| --------------------- | ------------------------------ |
| `GCP_SA_KEY`          | GCP Service Account JSON key   |
| `GCP_PROJECT`         | GCP Project ID                 |
| `GKE_CLUSTER_NAME`    | Cluster name (`anime-gke`)     |
| `GKE_CLUSTER_REGION`  | Cluster region (`us-central1`) |
| `ANIME_SECRETS_GROQ`  | Groq API key                   |
| `ANIME_SECRETS_HF`    | HuggingFace token              |
| `LANGCHAIN_SMITH_KEY` | LangSmith API key              |

### GCP Service Account Permissions

The service account (`github-actions-deployer`) needs:

- `roles/container.admin` (or `Kubernetes Engine Developer`)
- `roles/iam.serviceAccountUser`
- `roles/compute.viewer`

### Trigger Deployment

```bash
git push origin main
```

GitHub Actions will automatically apply changes to GKE.

---

## 🔐 Security Best Practices

- ✅ **No secrets in code**: All API keys via environment variables or K8s secrets
- ✅ **`.env` gitignored**: Local secrets never committed
- ✅ **GitHub Secrets**: CI/CD secrets stored securely
- ✅ **Kubernetes Secrets**: Runtime secrets injected into pods
- ✅ **Least privilege IAM**: Service account with minimal required roles

---

## 📊 Observability

### LangSmith Tracing

LangSmith provides full visibility into the RAG pipeline:

- Query latency breakdown
- Token usage per request
- Retrieved context documents
- LLM prompt/response pairs

Access traces at: [smith.langchain.com](https://smith.langchain.com)

### Health Checks

```bash
# Check API health
curl http://EXTERNAL_IP:8000/health

# Response
{"status": "OK", "pipeline_loaded": true}
```

---

## 🧪 API Usage

### Get Recommendations

```bash
curl -X POST http://EXTERNAL_IP:8000/recommend \
  -H "Content-Type: application/json" \
  -d '{"query": "Action anime with a strong protagonist and epic fights"}'
```

### Response Example

```json
{
  "answer": "Based on your preferences for action anime with a strong protagonist and epic fights, I recommend:\n\n1. **Attack on Titan** - Intense action with high stakes battles...\n2. **Demon Slayer** - Beautiful animation with incredible sword fights...\n3. **My Hero Academia** - Classic hero journey with amazing fight sequences..."
}
```

---

## 📋 Deployment Checklist

### Local Development

- [ ] Clone repository
- [ ] Create `.env` with API keys
- [ ] Run `uv sync`
- [ ] Build embeddings (if no `chroma_db/` exists)
- [ ] Start FastAPI server

### GKE Production

- [ ] GCP project with billing enabled
- [ ] Required APIs enabled (Container, Compute, IAM)
- [ ] GKE Autopilot cluster created (`anime-gke`)
- [ ] Persistent disk created with ChromaDB data
- [ ] Docker image pushed to DockerHub
- [ ] Kubernetes secrets created
- [ ] GitHub secrets configured
- [ ] GitHub Actions workflow deployed
- [ ] External IP accessible

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Farhan**

- GitHub: [@farhanrhine](https://github.com/farhanrhine)
- Email: mohammadfarhanalam09@gmail.com

---

<p align="center">
  Made with ❤️ and 🍜 for anime fans everywhere
</p>
