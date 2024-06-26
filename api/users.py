from typing import List

import fastapi
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import  AsyncSession
from fastapi import Depends, HTTPException

from api.utils.users import get_user, get_user_by_email, get_users, create_user
from api.utils.courses import get_user_courses
from db.db_setup import get_db,async_get_db
from pydantic_schemas.user import UserCreate, User
from pydantic_schemas.courses import Course


router = fastapi.APIRouter()



@router.get("/users", response_model=List[User], tags=["Get users"])
async def Get_users(db:Session = Depends(get_db),skip: int =0,limit:int=100):
    users = get_users(db, skip=skip,limit =limit)
    return users

@router.post("/users",response_model=User, status_code=201,tags=["Create user"])
async def create_new_user(user: UserCreate, db:Session = Depends(get_db) ):
    db_user = get_user_by_email(db=db,email =user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    return create_user(db=db,user=user)



@router.get("/users/{user_id}",response_model=User, tags=["Get users by ID"])
async def Get_user(user_id: int,db:AsyncSession = Depends(async_get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return db_user

@router.get("/users/{user_id}/courses",response_model =List[Course])
async def read_user_courses(user_id:int, db: Session=Depends(get_db)):
    courses = get_user_courses(db =db, user_id=user_id)
    return courses