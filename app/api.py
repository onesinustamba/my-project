from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1", tags=["api"])

@router.get("/hello")
async def hello_world():
    return {"message": "Hello World"}