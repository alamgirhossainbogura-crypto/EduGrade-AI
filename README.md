# 🎓 EduGrade AI: Autonomous Smart Classroom & Autopilot Assignment Grader

EduGrade AI is a production-grade, autonomous multi-agent system designed to revolutionize the educational grading ecosystem. Built specifically for the **Global AI Hackathon with Qwen Cloud**, this system automates the time-consuming process of reviewing student assignments and code repositories. 

By leveraging **Qwen Cloud's advanced reasoning flagship models** and hosted entirely on **Alibaba Cloud Infrastructure**, EduGrade AI delivers institutional-grade evaluations while ensuring absolute compliance through a robust **Human-in-the-Loop (HITL)** verification guardrail.

---

## 🚀 Core Features & Capabilities

### 🔍 1. Context-Aware Autonomous Evaluation
Unlike rigid keyword-matching scripts, EduGrade AI acts as a seasoned Teaching Assistant. It deeply analyzes code files, project architectures, semantic logic, and documentation. It scores submissions accurately against industry standards or custom academic rubrics.

### ✍️ 2. Granular Feedback Engine
The agent doesn't just hand out numbers; it explains the *why*. It automatically generates comprehensive, human-like reports pinpointing exact lines of code or paragraphs that need optimization, suggesting modern best practices and architectural fixes.

### 🛡️ 3. Strict Human-in-the-Loop (HITL) Guardrail
To eliminate AI hallucinations and ensure grading fairness, the system features an immutable approval gate. All AI-generated scores and feedback are stored in a **"Pending Approval"** state on a secure Teacher Dashboard. Educators retain full authority to override, modify, or approve the results.

### ✉️ 4. Autopilot Communication Agent
The moment an educator hits "Approve," a dedicated background worker triggers. It instantly compiles the report, formats a professional email, and safely dispatches the final grades directly to the student without any manual data entry.

---
## 🔄 Recent Hackathon Updates & Enhancements
​While the foundational concept of an education sync engine was explored previously, the platform has been completely re-engineered during this hackathon window:
​Migrated to Qwen Cloud: Completely overhauled the intelligence layer to utilize Qwen Cloud flagship models for superior code and logic reasoning.
​Alibaba Cloud Integration: Fully deployed and configured the live application infrastructure on Alibaba Cloud ECS.
​Multi-Agent Redesign: Transitioned from basic sequential scripting to an advanced multi-agent system (Grader Agent & Communicator Agent).
​Hardened HITL Guardrails: Built the secure interactive dashboard allowing educators to approve, edit, or reject AI evaluations before transmission.
## ​⚙️ Tech Stack & Infrastructure Specifications
​Languages: Python
​LLM Engine & APIs: Qwen Cloud API (Flagship Models)
​Cloud Infrastructure: Alibaba Cloud ECS (Elastic Compute Service)
​Frameworks & UI: FastAPI, Streamlit
​Agentic Orchestration: CrewAI, LangChain
​Data Validation: Pydantic
​Version Control & Hosting: Git, GitHub
## ​📁 Production Repository Structure
EduGrade-AI/
├── backend/
│   ├── app.py              # Asynchronous application entry point
│   ├── agents.py           # Core Qwen AI Agent & Tool definitions
│   ├── prompt_templates.py # Hardened systemic grading rubrics
│   └── requirements.txt    # Production dependency manifest
├── frontend/
│   └── ui.py               # Streamlit/FastAPI reactive user interfaces
├── docs/
│   └── architecture.png    # High-resolution system topology diagram
├── LICENSE                 # MIT Open Source License
└── README.md               # System documentation & deployment manifest

## 📦 Local Installation & Deployment Guide
​Prerequisites
​Python 3.10 or higher installed.
​Active Qwen Cloud API Key.
​Verified Alibaba Cloud Account credentials.
## ​1. Repository Setup
git clone [https://github.com/YOUR_USERNAME/EduGrade-AI.git](https://github.com/YOUR_USERNAME/EduGrade-AI.git)
cd EduGrade-AI

## 2. Dependency Resolution
pip install -r backend/requirements.txt
## 3. Environment Variable Configuration
​Create a .env file in the root directory:
QWEN_API_KEY=your_secured_qwen_cloud_api_token
ALIBABA_CLOUD_ECS_IP=your_allocated_instance_public_ip
SENDER_EMAIL_SMTP=your_configured_classroom_mail_gateway
## 4. Local Execution
streamlit run backend/app.py

## 🛠️ System Architecture

The entire core ecosystem is hosted securely on **Alibaba Cloud**, orchestrating continuous data loops between the frontend interfaces and the Qwen Cloud inference engines.

```text
       [ Student View ]                        [ Teacher Dashboard ]
              │                                          ▲
              │ (Submits Assignment/Repo)                │ (Reviews & Approves)
              ▼                                          │
   ┌─────────────────────────────────────────────────────────────┐
   │             ALIBABA CLOUD ECS (FastAPI Backend)             │
   └─────────────────────────────────────────────────────────────┘
              │                                          ▲
              ▼ (Dispatches Payloads)                    │ (Returns JSON)
   ┌─────────────────────────────────────────────────────────────┐
   │                   QWEN CLOUD AI INFERENCE                   │
   │                                                             │
   │  ┌───────────────────────┐       ┌───────────────────────┐  │
   │  │     Grader Agent      │       │  Communicator Agent   │  │
   │  │ (Reasoning/Evaluation)│       │ (Email/Report Writer) │  │
   │  └───────────────────────┘       └───────────────────────┘  │
   └─────────────────────────────────────────────────────────────┘
              │                                          │
              └───────────────────(Success)──────────────┘
                                  │
                                  ▼
                     [ Automated Email Dispatch ]

