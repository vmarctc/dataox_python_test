from database import Base
from sqlalchemy import String, Integer, Column, Text, Date


class Apartment(Base):
    __tablename__ = "apartment"

    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    title = Column(String)
    posted_date = Column(Date)
    location = Column(String)
    beds = Column(String)
    description = Column(Text)
    price = Column(String)

    def __repr__(self) -> str:
        return f"{self.title}"
