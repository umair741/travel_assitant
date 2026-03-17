from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from agent import create_travel_agent
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")

agent = create_travel_agent()

def clean_response(text):
    text = re.sub(r'\*\*?(.*?)\*\*?', r'\1', text)
    text = re.sub(r'#{1,3}\s?', '', text)
    text = re.sub(r'--+', '', text)
    return text.strip()

class UserQuery(BaseModel):
    input: str

@app.post("/ask")
async def ask_agent(query: UserQuery):
    try:
        response = await run_in_threadpool(agent.invoke, {"input": query.input})
        return {"response": clean_response(response["output"])}
    except Exception as e:
        return {"error": str(e)}