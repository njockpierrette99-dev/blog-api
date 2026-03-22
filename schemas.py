from pydantic import BaseModel
from typing import Optional

class ArticleCreate(BaseModel):
    titre: str
    contenu: str
    auteur: str
    date: Optional[str] = None
    categorie: Optional[str] = None
    tags: Optional[str] = None

class ArticleUpdate(BaseModel):
    titre: Optional[str] = None
    contenu: Optional[str] = None
    categorie: Optional[str] = None
    tags: Optional[str] = None

class ArticleResponse(BaseModel):
    id: int
    titre: str
    contenu: str
    auteur: str
    date: str
    categorie: Optional[str] = None
    tags: Optional[str] = None

    class Config:
        from_attributes = True
