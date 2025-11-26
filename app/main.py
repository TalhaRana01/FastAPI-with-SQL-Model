from fastapi import FastAPI

from app.database.config import create_tables
from contextlib import asynccontextmanager
from app.user.services import create_user_service, get_all_users

@asynccontextmanager
async def lifespan(app: FastAPI):
  create_tables()
  yield


app = FastAPI(lifespan=lifespan)


@app.post("/user")
def create_user(new_user : dict):
  user = create_user_service(name=new_user["name"], email=new_user["email"])
  return user

@app.get("/users")
def get_users():
  users = get_all_users()
  return users
  
  
  