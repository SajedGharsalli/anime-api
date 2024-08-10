from fastapi import FastAPI
from app.api.animeApi import animeRouter
from app.api.mangaApi import mangaRouter
from app.api.charApi import charRouter

app=FastAPI()
app.include_router(animeRouter)
app.include_router(mangaRouter)
app.include_router(charRouter)

@app.get('/')
def index():
    return {"status":"anime api running"}