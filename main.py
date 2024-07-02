from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role , UserUpdate
from uuid import UUID, uuid4


app = FastAPI()


db: List[User] = [
    User(
        id=UUID("da6d525e-4349-4a09-a353-f7ea2197448b"),
        first_name="Hasnain",
        last_name="Hasib",
        middle_name = "",
        gender=Gender.male,
        role=[Role.admin, Role.user]
    ),
    User(
        id=UUID("d57d866b-0d51-42fd-b9ab-7adc985630f4"),
        first_name="Maria",
        last_name="Carmen",
        middle_name = "",
        gender=Gender.female,
        role=[Role.student]
    )
]


@app.get("/")
async def root():
    return {"API": "FastAPI"}


@app.get("/users/info")
async def user_data():
    return db

@app.post("/users/info")
async def create_user(user :User):
        db.append(user)
        return {"id": user.id}
    
@app.delete("/users/info{user_id}")
async def delet_user(user_id : UUID):
    for user in db :
        if user.id == user_id:
            db.remove(user)
            return 
        
    raise HTTPException(
        
        status_code=404,
        detail=f"user with id {user_id} does not exists"
    )
    
@app.put("/users/info/{user_id}")
async def user_update(user_id: UUID, update_user: UserUpdate):
    for user in db:
        if user.id == user_id:
            if update_user.first_name is not None:
                user.first_name = update_user.first_name
            if update_user.last_name is not None:
                user.last_name = update_user.last_name
            if update_user.middle_name is not None:
                user.middle_name = update_user.middle_name
            if update_user.gender is not None:
                user.gender = update_user.gender
            if update_user.role is not None:
                user.role = update_user.role
            return {"message": "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")