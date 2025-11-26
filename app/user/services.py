from sqlmodel import Session, select
from app.database.config import engine
from app.user.models import User



# Create User
def create_user_service(name: str, email:str):
  user = User(name=name, email=email)
  with Session(engine) as session:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Get all Users
def get_all_users():
  with Session(engine) as session:
    statement = select(User)
    users = session.exec(statement)
    return users.all()

    
  
    
  
  
  
  