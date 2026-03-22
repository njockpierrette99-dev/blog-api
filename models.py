from sqlalchemy import Column, Integer, String, Text
from database import Base
import datetime

class Article(Base):
    __tablename__ = "articles"

    id        = Column(Integer, primary_key=True, index=True)
    titre     = Column(String(200), nullable=False)
    contenu   = Column(Text, nullable=False)
    auteur    = Column(String(100), nullable=False)
    date      = Column(String(20), default=str(datetime.date.today()))
    categorie = Column(String(100), nullable=True)
    tags      = Column(String(200), nullable=True)
