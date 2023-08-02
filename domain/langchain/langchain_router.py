from fastapi import APIRouter

router = APIRouter(
    prefix="/api/langchain",
)

@router.get("/test")
def test():
    
    return {"message": "Hello World"}