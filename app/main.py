from fastapi import FastAPI
from app.api import router

app = FastAPI(title="My Project")

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}