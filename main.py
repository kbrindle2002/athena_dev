from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<h1>Welcome to ATHENA on Azure with FastAPI 🚀</h1>"