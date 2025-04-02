from fastapi import HTTPException, APIRouter
from typing import Any

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
async def read_items():
    return [{"name": "Item Foo"}, {"name": "item Bar"}]