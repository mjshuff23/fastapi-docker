import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import User as ModelUser
from schema import User as SchemaUser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


# Create a user
@app.post("/user/", response_model=SchemaUser)
def create_user(user: SchemaUser):
    db_user = ModelUser(
        first_name=user.first_name, last_name=user.last_name, age=user.age
    )
    db.session.add(db_user)
    db.session.commit()
    return user


# List all users
@app.get("/users/")
def get_users():
    users = db.session.query(ModelUser).all()
    return users


# Get a user by id
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = db.session.query(ModelUser).get(user_id)
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
