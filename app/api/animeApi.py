from fastapi import APIRouter,HTTPException
from app.service.jikan_service import fetch_data
import urllib.parse

animeRouter= APIRouter(prefix="/anime")

@animeRouter.get("/{page}")
def get_top(page: int):
    endpoint =f"top/anime?page={page}"
    res = fetch_data(endpoint)
    data = res["data"]
    anime_list = []
    for anime in data :
        anime_list.append({
            "title":anime['title'],
            "title_english":anime["title_english"],
            "studios" : [studio["name"] for studio in anime["studios"]],
            "image": anime["images"]["jpg"]["image_url"],
            "trailer" : anime['trailer']["youtube_id"],
            "synopsis":anime["synopsis"],
            "episodes" : anime["episodes"],
            "status" : anime["status"],
            "year" : anime["year"],
            "rank" : anime["rank"],
            "genres" : [genre["name"] for genre in anime["genres"]]
        })
    return anime_list

@animeRouter.get("/search_by_name/{name}")
def get_by_name(name: str):
    query = urllib.parse.quote(name.strip())
    endpoint = f"anime?q={query}&sfw"
    res = fetch_data(endpoint)
    data = res["data"]
    anime_list = []
    for anime in data :
        anime_list.append({
            "title":anime['title'],
            "title_english":anime["title_english"],
            "studios" : [studio["name"] for studio in anime["studios"]],
            "image": anime["images"]["jpg"]["image_url"],
            "trailer" : anime['trailer']["youtube_id"],
            "synopsis":anime["synopsis"],
            "episodes" : anime["episodes"],
            "status" : anime["status"],
            "year" : anime["year"],
            "rank" : anime["rank"],
            "genres" : [genre["name"] for genre in anime["genres"]]
        })
    return anime_list

# @animeRouter.get("/search_by_genres")