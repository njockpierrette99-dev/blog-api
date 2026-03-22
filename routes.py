from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Article
from schemas import ArticleCreate, ArticleUpdate, ArticleResponse
from typing import List, Optional
import datetime

router = APIRouter()

# Créer un article
@router.post("/api/articles", status_code=201)
def creer_article(article: ArticleCreate, db: Session = Depends(get_db)):
    nouvel_article = Article(
        titre=article.titre,
        contenu=article.contenu,
        auteur=article.auteur,
        date=article.date or str(datetime.date.today()),
        categorie=article.categorie,
        tags=article.tags
    )
    db.add(nouvel_article)
    db.commit()
    db.refresh(nouvel_article)
    return {"message": "Article créé avec succès", "id": nouvel_article.id}

# Lire tous les articles
@router.get("/api/articles", response_model=List[ArticleResponse])
def lire_articles(
    categorie: Optional[str] = None,
    auteur: Optional[str] = None,
    date: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Article)
    if categorie:
        query = query.filter(Article.categorie == categorie)
    if auteur:
        query = query.filter(Article.auteur == auteur)
    if date:
        query = query.filter(Article.date == date)
    return query.all()

# Lire un article par ID
@router.get("/api/articles/{id}", response_model=ArticleResponse)
def lire_article(id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    return article

# Modifier un article
@router.put("/api/articles/{id}")
def modifier_article(id: int, data: ArticleUpdate, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    if data.titre:
        article.titre = data.titre
    if data.contenu:
        article.contenu = data.contenu
    if data.categorie:
        article.categorie = data.categorie
    if data.tags:
        article.tags = data.tags
    db.commit()
    return {"message": "Article modifié avec succès"}

# Supprimer un article
@router.delete("/api/articles/{id}")
def supprimer_article(id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    db.delete(article)
    db.commit()
    return {"message": "Article supprimé avec succès"}

# Rechercher un article
@router.get("/api/articles/search/query")
def rechercher_articles(query: str, db: Session = Depends(get_db)):
    resultats = db.query(Article).filter(
        Article.titre.contains(query) | Article.contenu.contains(query)
    ).all()
    return resultats
