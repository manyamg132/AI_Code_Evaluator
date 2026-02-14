from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from evaluate import evaluate_code_file, evaluate_code_text

app = FastAPI(title="AI Coding Assignment Evaluator")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict to frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AI Coding Assignment Evaluator is running."}

@app.post("/evaluate")
async def evaluate(file: UploadFile = File(...)):
    content = await file.read()
    code_text = content.decode("utf-8")
    feedback_text = evaluate_code_text(code_text, language="python")
    return {"feedback": feedback_text}

@app.post("/upload_github")
async def upload_github(payload: dict):
    url = payload.get("github_url", "")
    feedback_text = await evaluate_code_file(url, language="python")
    return {"feedback": feedback_text}

