
# Blog API

API backend pour gérer un blog simple, développée avec **FastAPI** et **SQLite**.


# Technologies utilisées

| **Python** | 
| **FastAPI** | 
| **SQLite** | 
| **SQLAlchemy** | 
| **Pydantic** | 
| **Uvicorn** |


# Installation

1- Cloner le dépôt

    git clone https://github.com/njockpierrette99-dev/blog-api.git
    cd blog-api


2- Installer les dépendances

    pip install fastapi uvicorn sqlalchemy


3- Lancer le serveur

    uvicorn main:app --reload


Le serveur est accessible sur : http://127.0.0.1:8000


# Documentation interactive

FastAPI génère automatiquement une documentation interactive :

Interface URL
Swagger UI http://127.0.0.1:8000/docs
ReDoc http://127.0.0.1:8000/redoc


# Base de données SQLite

Le projet utilise SQLite comme base de données. Le fichier blog.db est automatiquement créé au premier lancement.

#  Endpoints de l'API

  Créer un article


    POST /api/articles


  Lister tous les articles


    GET /api/articles


  Voir un article spécifique


    GET /api/articles/{id}


  Modifier un article


    PUT /api/articles/{id}


  Supprimer un article

    DELETE /api/articles/{id}


  Rechercher des articles

    GET /api/articles/search?query={texte}


# Structure du projet

blog-api/
├── main.py           # Point d'entrée (configuration FastAPI)
├── database.py       # Connexion SQLite et session SQLAlchemy
├── models.py         # Définition de la table Article
├── schemas.py        # Schémas Pydantic (validation des données)
├── routes.py         # Définition des endpoints
├── blog.db           # Base de données SQLite (créée automatiquement)
└── README.md


# Tester avec Swagger

1- Lance le serveur : 

    uvicorn main:app --reload

2. Ouvre : http://127.0.0.1:8000/docs


# Auteur

NDJOCK MIRIELLE GLADICE
UE : INF222 - Développement Backend

# Date

Mars 2026
