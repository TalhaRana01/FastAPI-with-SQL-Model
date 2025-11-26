from sqlmodel import create_engine, SQLModel
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# print(BASE_DIR)

db_path = os.path.join(BASE_DIR, "sqlite.db")

DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(DATABASE_URL, echo=True)


# Create Table 
def create_tables():
  SQLModel.metadata.create_all(engine)
