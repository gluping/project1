from database import Base
from sqlalchemy.sql.expression import null, text
from sqlalchemy import Column, Integer, String, Boolean,Text
from sqlalchemy.sql.sqltypes import TIMESTAMP


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable = False)
    email = Column(String, nullable = False, unique=True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    goal = Column(String(10))
    recommendation_type = Column(String(10))
    recommendation_text = Column(Text)
