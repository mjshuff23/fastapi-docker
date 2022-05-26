from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(
        String,
    )
    last_name = Column(String)
    age = Column(Integer)
