from fastapi import FastAPI
from database import engine, Base
from routes import router

# Crée toutes les tables dans la base de données
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog API",
    description="API backend pour gérer un blog simple",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def accueil():
    return {"message": "Bienvenue sur l'API Blog !"}
