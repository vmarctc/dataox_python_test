from database import Base, engine
# from models import Apartment

Base.metadata.create_all(engine)
