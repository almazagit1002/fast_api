import fastapi
from typing import Optional, List
from pydantic import BaseModel



router = fastapi.APIRouter()



users = []

class User(BaseModel):
    email : str
    is_active : bool
    bio: Optional[str] = None

@router.get("/users", response_model=List[User], tags=["Get users"])
async def get_user():
    return users

@router.post("/users", tags=["Create user"])
async def create_user(user: User):
    users.append(user)
    return "Success"


@router.get("/users/{id}", tags=["Get users by ID"])
async def get_user(id: int):
    return {"useru": users[id]}