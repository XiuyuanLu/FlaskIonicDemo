from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 't_user_auth'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    username = Column(String(255), unique=True)
    password = Column(String(45))

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)