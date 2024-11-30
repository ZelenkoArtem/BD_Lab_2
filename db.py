from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Налаштування підключення до бази даних PostgreSQL
DATABASE_URL = "postgresql://postgres:qwerty@localhost:5432/postgres"

# Створення об'єкта двигуна бази даних
engine = create_engine(DATABASE_URL)

# Налаштування сесії
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ініціалізація бази даних (створення таблиць)
def init_db():
    Base.metadata.create_all(bind=engine)
