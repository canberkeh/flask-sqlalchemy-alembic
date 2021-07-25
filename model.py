from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import engine, create_engine


engine = create_engine('sqlite:///database.db')
Base = declarative_base()
metadata = Base.metadata



class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    #alembic revision -m "initial commit"  