from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://postgres:vmar26@localhost/scraper_db"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()
