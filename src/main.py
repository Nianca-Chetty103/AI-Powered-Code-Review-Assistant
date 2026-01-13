from fastapi import FastAPI, Request
from dotenv import load_dotenv
from app.github import handle_pull_request

load_dotenv()

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    if "pull_request" in payload:
        await handle_pull_request(payload)

    return {"status": "ok"}


