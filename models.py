from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR,Integer

Base = declarative_base()

class Cake(Base):
    __tablename__ = "cakes"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(Text, index=True)
    flavor = Column(Text)
    price = Column(Integer)
    imageUrl = Column(VARCHAR)