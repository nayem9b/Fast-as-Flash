from fastapi import FastAPI
from pydantic import BaseModel

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