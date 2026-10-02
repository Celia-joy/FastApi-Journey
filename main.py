from re import I
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def home():
    return { "message" : "Hello, FastAPI! "}

@app.get("/about")
def about():
    return {
        "name" : "Celia" ,
        "project" : "FastAPI Journey"
    }
"""
@app.get("/users")
def get_users():
    return {
        "users": ["Celia", "Alice", "Bob"]
    }

@app.post("/users")
def create_user():
    return {
        "message" : "User created"
    }

@app.put("/users/{user_id}")
def update_user(user_id: int):
    return {
        "message": f"Replacing user {user_id}"
    }

@app.patch("/users/{user_id}")
def partially_update_user(user_id: int):
    return {
        "message": f"Partially updating user {user_id}"
    }

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {
        "message": f"User {user_id} deleted"
    }

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
        "product_id": product_id,
        "message" : "Product found"
    }

@app.get("/products")
def get_products(category: str):
    return {
        "category": category,
        "message": "Showing products"
    }
"""

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }

class Product(BaseModel):
    name: str
    price: float
    category: str

@app.post("/products")
def create_product(product: Product):
    return {
        "message": "Product created successfully",
        "product": product
    }
