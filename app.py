from fastapi import FastAPI
from pydantic import BaseModel
from agent import create_travel_agent
from fastapi.concurrency import run_in_threadpool

app = FastAPI()
agent = create_travel_agent()

class UserQuery(BaseModel):
    input: str

@app.post("/ask")
async def ask_agent(query: UserQuery):
    try:
        response = await run_in_threadpool(agent.invoke, {"input": query.input})
        return {"response": response["output"]}
    except Exception as e:
        return {"error": str(e)}
