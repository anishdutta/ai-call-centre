import ssl
from fastapi import FastAPI
from src.whisper import whisper_service
from src.openai import openai_service
from pydantic import BaseModel

class Chatbot(BaseModel):
    history: list

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

app = FastAPI()

@app.get("/")
async def root():
    return {
        "success": True
    }

@app.post("/transcribe")
async def root():
    whisper = whisper_service()
    response = whisper.transcribe()
    return{
        response
    }

@app.post('/chatbot')
async def root(request:Chatbot):
    print("hello",request)
    # validation layer (optional)
    result = openai_service.Openai_Service().chatbot(chat_history=request.history)
    return {"response": result}
