import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.agents import run_grading_pipeline, run_communication_pipeline

app = FastAPI(title="EduGrade AI Production Backend")

# In-Memory Database for Hackathon Simulation
db_submissions = {}

class SubmissionPayload(BaseModel):
    student_id: str
    submission_data: str
    rubric: str

class ApprovalPayload(BaseModel):
    student_id: str
    final_score: int
    final_feedback: str

@app.post("/api/submit")
async def submit_assignment(payload: SubmissionPayload):
    try:
        # Trigger Autonomous Agent Layer
        raw_analysis = run_grading_pipeline(payload.submission_data, payload.rubric)
        
        # Save into pending state (Human-in-the-Loop Gate)
        db_submissions[payload.student_id] = {
            "status": "Pending Approval",
            "ai_score": raw_analysis.get("score", 0),
            "ai_feedback": raw_analysis.get("feedback", "No feedback extracted."),
            "submission_data": payload.submission_data
        }
        
        return {"status": "Success", "message": "Evaluation generated. Pending teacher approval workflow."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/pending/{student_id}")
async def get_pending_submission(student_id: str):
    if student_id not in db_submissions:
        raise HTTPException(status_code=404, detail="Submission profile not found.")
    return db_submissions[student_id]

@app.post("/api/approve")
async def approve_and_dispatch(payload: ApprovalPayload):
    if payload.student_id not in db_submissions:
        raise HTTPException(status_code=404, detail="Record context missing.")
        
    try:
        # Trigger Autopilot Communication Agent
        email_draft = run_communication_pipeline(payload.final_score, payload.final_feedback)
        
        # Update Database State
        db_submissions[payload.student_id].update({
            "status": "Approved & Dispatched",
            "final_score": payload.final_score,
            "final_feedback": payload.final_feedback,
            "dispatch_email": email_draft
        })
        
        return {"status": "Dispatched", "email_payload": email_draft}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
