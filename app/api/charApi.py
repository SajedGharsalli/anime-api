from fastapi import APIRouter
from app.service.jikan_service import fetch_data
import urllib.parse

charRouter = APIRouter(prefix='/characters')

@charRouter.get("/top/{page}")
def get_top(page: int):
    endpoint =f"top/characters?page={page}"
    res = fetch_data(endpoint)
    data = res["data"]
    char_list = []
    for char in data :
        char_list.append({
            "name": char["name"],
            "image": char['images']['jpg']['image_url'],
            "nicknames" : char["nicknames"]
        })
    return char_list

@charRouter.get('/search_by_name/{name}')
def get_by_name(name: str):
    query = urllib.parse.quote(name.strip())
    endpoint = f"characters?q={query}&sfw"
    res = fetch_data(endpoint)
    data = res["data"]
    char_list = []
    for char in data :
        char_list.append({
            "name": char["name"],
            "image": char['images']['jpg']['image_url'],
            "nicknames" : char["nicknames"]
        })
    return char_list
