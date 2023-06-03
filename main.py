from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI RB",
    description="Building app for managing students and courses.!",
    version="0.0.1",
    contact={
        "name": "Rajesh Baghel",
        "email": "rajeshb3297@gmail.com",
    },
    license_info={
        "name": "MIT",
    }
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get("/users", response_model= List[User])
async def get_users():
    return users

@app.post("/users")
async def create_users(user: User):
    users.append(user)
    return "Success"

@app.get("/users/{id}")
async def get_user(id: int = Path(..., description="The ID of the user you want to retrieve", gt=1),
                   q: str = Query(None, max_length= 4)):
    return {"User": users[id],"query": q}