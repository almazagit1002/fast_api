from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


users = []

class User(BaseModel):
    email : str
    is_active : bool
    bio: Optional[str] = None

@app.get("/users", response_model=List[User])
async def get_user():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}")
async def get_user(id: int):
    return users[id]