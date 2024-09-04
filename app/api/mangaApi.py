from fastapi import APIRouter
from app.service.jikan_service import fetch_data
import urllib.parse
mangaRouter = APIRouter(prefix="/manga")


@mangaRouter.get('/goat/')
def get_top():
    endpoint =f"top/manga?page=1&sfw"
    res = fetch_data(endpoint)
    data = res["data"]
    manga_list = []
    for manga in data :
        title = manga.get('title_english')
        if not title:
            continue
        manga_list.append({
            "title":manga['title_english'],
            "authors" : [author["name"] for author in manga["authors"]],
            "image": manga["images"]["jpg"]["image_url"],
            "synopsis":manga["synopsis"],
            "chapters" : manga["chapters"],
            "status" : manga["status"],
            "year" : manga["published"]["prop"]["from"]["year"],
            "rank" : manga["rank"],
            "score" : manga["score"],
            "genres" : [genre["name"] for genre in manga["genres"]]
        })
        manga_list_sorted = sorted(manga_list, key=lambda x: x['score'], reverse=True)
    return manga_list_sorted

@mangaRouter.get('/{page}')
def get_top(page:int):
    endpoint =f"top/manga?page={page}&sfw"
    res = fetch_data(endpoint)
    data = res["data"]
    manga_list = []
    for manga in data :
        title = manga.get('title_english')
        if not title:
            continue
        manga_list.append({
            "title":manga['title_english'],
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

@mangaRouter.get("/search/{name}")
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