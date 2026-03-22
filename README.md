# Blog API

API backend pour gérer un blog simple, développée avec FastAPI et SQLite.

## Installation
```bash
pip3 install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
```

## Endpoints

| Méthode | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/articles | Créer un article |
| GET | /api/articles | Lister tous les articles |
| GET | /api/articles/{id} | Lire un article |
| PUT | /api/articles/{id} | Modifier un article |
| DELETE | /api/articles/{id} | Supprimer un article |
| GET | /api/articles/search/query | Rechercher un article |

## Documentation

Swagger disponible sur : http://127.0.0.1:8000/docs

## Auteur

NDJOCK MIRIELLE GLADICE
