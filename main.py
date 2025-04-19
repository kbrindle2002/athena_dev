from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import json

app = FastAPI()

# Serve the static frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# POST /api/ask
@app.post("/api/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data.get("question", "")
    if not question:
        return JSONResponse({"error": "No question provided"}, status_code=422)
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": "user_question",
        "question": question
    }
    with open("athena_memory_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
    return {"echo": question}

# Module endpoints
@app.get("/api/modules/fake-news")
async def fake_news():
    return {"name": "Fake News Detector", "status": "active"}

@app.get("/api/modules/bias-mapping")
async def bias_mapping():
    return {"name": "Bias Mapping", "status": "active"}

@app.get("/api/modules/narrative-tracker")
async def narrative_tracker():
    return {"name": "Narrative Tracker", "status": "active"}

@app.get("/api/modules/security-core")
async def security_core():
    return {"name": "Security Core", "status": "active"}
