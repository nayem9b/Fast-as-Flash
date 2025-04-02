from fastapi import APIRouter, FastAPI, HTTPException, Body, Path, Query
from typing import Dict, List, Optional
from pydantic import BaseModel

# Sample data model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    available: bool = True

# Sample database
items_db: Dict[int, Item] = {
    1: Item(id=1, name="Item 1", description="First item", price=19.99, available=True),
    2: Item(id=2, name="Item 2", description="Second item", price=29.99, available=True),
    3: Item(id=3, name="Item 3", description="Third item", price=39.99, available=False),
}

app = FastAPI()
api_router = APIRouter()

@app.get("/")
def root():
    return {"message": "Hello World"}

# GET all items
@app.get("/items", response_model=List[Item])
def get_items(skip: int = 0, limit: int = 10, available: Optional[bool] = None):
    """
    Retrieve all items with optional filtering by availability.
    """
    if available is None:
        return list(items_db.values())[skip:skip+limit]
    return [item for item in items_db.values() if item.available == available][skip:skip+limit]

# GET item by ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int = Path(..., title="The ID of the item to get", ge=1)):
    """
    Retrieve a specific item by its ID.
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# POST - Create a new item
@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item = Body(..., title="The item to create")):
    """
    Create a new item.
    """
    if item.id in items_db:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items_db[item.id] = item
    return item

# DELETE - Remove an item
@app.delete("/items/{item_name}", status_code=204)
def delete_item(item_name: str = Path(..., title="The name of the item to delete")):
    """
    Delete an item by its name.
    """
    for item_id, item in items_db.items():
        if item.name == item_name:
            del items_db[item_id]
            return None
    raise HTTPException(status_code=404, detail="Item not found")
    return None