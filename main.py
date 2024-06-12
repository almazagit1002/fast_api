from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel




tags_metadata = [
    {
        "name": "Get users",
        "description": "Get all users",
    },
    {
        "name": "Create user",
        "description": "Create a new user",
       
    },
     {
        "name": "Get users by ID",
        "description": "Get user by ID",
       
    },
]

app = FastAPI(
    title= "Fast API LMS",
    description="LMS for managing students and courses",
    version="0,0.1",
    contact={
        "name": "Alejandro",
        "email": "almazagit1002@gmail.com"
    },
    license_info={
        "name": "MIT"
    },
    )


users = []

class User(BaseModel):
    email : str
    is_active : bool
    bio: Optional[str] = None

@app.get("/users", response_model=List[User], tags=["Get users"])
async def get_user():
    return users

@app.post("/users", tags=["Create user"])
async def create_user(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}", tags=["Get users by ID"])
async def get_user(
    id: int = Path (..., description = "The ID of the user you want to retrieve", gt=0),
    q : str = Query(None, max_length=5) 
    ):
    return {"useru": users[id], "query": q }