import os
from langchain_community.llms import OpenAI
from crewai import Agent, Task, Crew, Process
from pydantic import BaseModel, Field

# Ensure API Key is loaded
QWEN_API_KEY = os.getenv("QWEN_API_KEY")

# Initialize Qwen Cloud Client using OpenAI Compatible Interface
qwen_llm = OpenAI(
    openai_api_key=QWEN_API_KEY,
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model_name="qwen-max"  # Flagship model for advanced reasoning
)

# Pydantic Structure for Grader Output
class GradingResult(BaseModel):
    score: int = Field(..., description="Score out of 100 based on standard rubrics.")
    feedback: str = Field(..., description="Detailed, granular feedback regarding logic, architecture, and code quality.")

# 1. Define Grader Agent
grader_agent = Agent(
    role="Expert Academic & Technical Code Reviewer",
    goal="Analyze student assignment repositories or code artifacts deeply against rubrics and point out exact flaws and optimizations.",
    backstory="You are a veteran Teaching Assistant and Senior Systems Architect. You read through logic structural issues, detect patterns, and provide precise, non-generic feedback without any AI hallucinations.",
    verbose=True,
    allow_delegation=False,
    llm=qwen_llm
)

# 2. Define Communicator Agent
communicator_agent = Agent(
    role="Automated Autopilot Communication Officer",
    goal="Formulate highly professional, encouraging, and structured notification emails containing finalized grading reports.",
    backstory="You take rough grader points and approved metrics, then convert them into flawless, polite, and institution-grade student notification dispatches.",
    verbose=True,
    allow_delegation=False,
    llm=qwen_llm
)

def run_grading_pipeline(student_submission: str, rubric_criteria: str):
    # Task for Grading
    grading_task = Task(
        description=f"Evaluate the following student submission:\n{student_submission}\n\nAgainst these specific rubrics:\n{rubric_criteria}",
        expected_output="A structured JSON object matching the GradingResult schema containing score and detailed markdown feedback.",
        agent=grader_agent,
        output_json=GradingResult
    )

    crew = Crew(
        agents=[grader_agent],
        tasks=[grading_task],
        process=Process.sequential
    )
    
    result = crew.kickoff()
    return result

def run_communication_pipeline(approved_score: int, approved_feedback: str):
    # Task for Notification
    dispatch_task = Task(
        description=f"Draft a formal dispatch email. Approved Score: {approved_score}/100. Feedback Summary:\n{approved_feedback}",
        expected_output="A ready-to-send email body with Subject and Greetings.",
        agent=communicator_agent
    )

    crew = Crew(
        agents=[communicator_agent],
        tasks=[dispatch_task],
        process=Process.sequential
    )

    return crew.kickoff()
