from fastapi import APIRouter
from app.service.jikan_service import fetch_data
import urllib.parse
mangaRouter = APIRouter(prefix="/manga")

@mangaRouter.get('/{page}')
def get_top(page:int):
    endpoint =f"top/manga?page={page}"
    res = fetch_data(endpoint)
    data = res["data"]
    manga_list = []
    for manga in data :
        manga_list.append({
            "title":manga['title'],
            "title_english":manga["title_english"],
            "authors" : [author["name"] for author in manga["authors"]],
            "image": manga["images"]["jpg"]["image_url"],
            "synopsis":manga["synopsis"],
            "chapters" : manga["chapters"],
            "status" : manga["status"],
            "year" : manga["published"]["prop"]["from"]["year"],
            "rank" : manga["rank"],
            "genres" : [genre["name"] for genre in manga["genres"]]
        })
    return manga_list

@mangaRouter.get("/search_by_name/{name}")
def get_by_name(name:str ):
    query = urllib.parse.quote(name.strip())
    endpoint = f"manga?q={query}&sfw"
    res = fetch_data(endpoint)
    data = res["data"]
    manga_list = []
    for manga in data :
        manga_list.append({
            "title":manga['title'],
            "authors" : [author["name"] for author in manga["authors"]],
            "image": manga["images"]["jpg"]["image_url"],
            "synopsis":manga["synopsis"],
            "chapters" : manga["chapters"],
            "status" : manga["status"],
            "year" : manga["published"]["prop"]["from"]["year"],
            "rank" : manga["rank"],
            "genres" : [genre["name"] for genre in manga["genres"]]
        })
    return manga_list