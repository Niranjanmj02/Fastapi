# app/routes.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Example API route
@router.get("/api/data")
async def get_data():   
    return {"message": "Hello from fast!"}