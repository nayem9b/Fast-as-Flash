from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

class Review(BaseModel):
    name_stars: str
    text: str
    public: bool = False

class MovieReview(BaseModel):
    movie: str
    review = Review

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/hello")
def root(name:str = "Nayem"):
    return {"message": f"Hello {name}"}

@app.post("/reviews")
def create_review(review: MovieReview):
    db_review=crud.create_review(review)
    return db_review


# from fastapi import FastAPI
# from pydantic import BaseModel

# # Define model Item
# class Item(BaseModel):
#     name: str

# app = FastAPI()


# @app.post("/")
# def root(item: Item):
#     name = item.name


class Item(BaseModel):
    name: str

# Define items at application start
items = {"apples", "oranges", "bananas"}
class Item(BaseModel):
    name: str
    quantity: Optional[int] = 0
items = {"scissors": Item(name="scissors", quantity=100)}



@app.delete("/items")
def delete_item(item: Item):
    name = item.name
    if name in items:
        items.remove(name)
    else:
        # Raise HTTPException with status code for "not found"
        raise HTTPException(status_code=404, detail="Item not found.")
    return {}