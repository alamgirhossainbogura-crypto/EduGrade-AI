import streamlit as st
import requests

# Production Endpoints
BACKEND_URL = "http://localhost:8000"  # Map to Alibaba Cloud ECS internal or global IP

st.set_page_config(page_title="EduGrade AI - Teacher Control Panel", layout="wide")

st.title("🎓 EduGrade AI: Teacher Cockpit & HITL Dashboard")
st.subheader("Autonomous Multi-Agent Evaluation Gateway on Qwen Cloud")

st.sidebar.header("Navigation Hub")
app_mode = st.sidebar.radio("Choose Dashboard View", ["Simulation Terminal", "Pending Verifications"])

if app_mode == "Simulation Terminal":
    st.header("📥 Student Repository Submission Emulator")
    
    student_id = st.text_input("Unique Student ID (e.g., STU-2027)")
    submission_data = st.text_area("Paste Python Code Repository Structure or Essay text")
    rubric = st.text_area("System Rubric Rules", value="1. Code optimization & clean architecture (50 points)\n2. Logic correctness (50 points)")
    
    if st.button("Trigger Autonomous Evaluation Pipeline"):
        if student_id and submission_data:
            with st.spinner("Qwen Cloud Multi-Agent processing context..."):
                payload = {"student_id": student_id, "submission_data": submission_data, "rubric": rubric}
                response = requests.post(f"{BACKEND_URL}/api/submit", json=payload)
                if response.status_code == 200:
                    st.success("Pipeline executed successfully! Data held in 'Pending Approval' state.")
                else:
                    st.error("Error connecting with backend engine.")

elif app_mode == "Pending Verifications":
    st.header("🛡️ Human-in-the-Loop Enforcement Gate")
    target_student = st.text_input("Enter Student ID to review")
    
    if st.button("Fetch Queue Metrics"):
        response = requests.get(f"{BACKEND_URL}/api/pending/{target_student}")
        if response.status_code == 200:
            record = response.json()
            st.info(f"Current Lifecycle Status: {record['status']}")
            
            st.text_area("Original Submission Artifact", value=record['submission_data'], disabled=True)
            
            # Interactive overrides
            editable_score = st.number_input("Review and Override Score (0-100)", value=int(record['ai_score']))
            editable_feedback = st.text_area("Review and Edit Agent-Generated Feedback", value=record['ai_feedback'], height=300)
            
            if st.button("Approve & Autopilot Dispatch"):
                approve_payload = {
                    "student_id": target_student,
                    "final_score": editable_score,
                    "final_feedback": editable_feedback
                }
                dispatch_res = requests.post(f"{BACKEND_URL}/api/approve", json=approve_payload)
                if dispatch_res.status_code == 200:
                    st.success("Verification complete. Communicator agent has safely dispatched reports to student log.")
                    st.markdown("### Dispatched Report Blueprint:")
                    st.code(dispatch_res.json()["email_payload"])
        else:
            st.warning("No files or data found for this identifier workflow queue.")
