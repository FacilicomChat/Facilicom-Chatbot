from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Optional
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Facilicom Chatbot", version="1.0.0")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "Jij bent de Facilicom Chatbox, een vriendelijke, professionele Nederlandstalige assistent."
)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatTurn(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[ChatTurn]] = None
    temperature: Optional[float] = 0.7

@app.get("/health")
async def health():
    return {"status": "ok", "model": MODEL_NAME}

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        messages: List[Dict[str, str]] = []
        if SYSTEM_PROMPT:
            messages.append({"role": "system", "content": SYSTEM_PROMPT})
        if req.history:
            for t in req.history:
                if t.role in ("user", "assistant", "system") and t.content:
                    messages.append({"role": t.role, "content": t.content})
        messages.append({"role": "user", "content": req.message})
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=req.temperature or 0.7,
        )
        return {"reply": completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
