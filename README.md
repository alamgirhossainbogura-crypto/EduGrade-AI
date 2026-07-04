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
