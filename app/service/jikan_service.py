import requests
from fastapi import HTTPException


JIKAN_BASE_URL= "https://api.jikan.moe/v4"

def fetch_data(endpoint : str):
    res = requests.get(f"{JIKAN_BASE_URL}/{endpoint}")
    if res.status_code !=200 :
        raise HTTPException(status_code=res.status_code,detail="error fetching data")
    return res.json()
