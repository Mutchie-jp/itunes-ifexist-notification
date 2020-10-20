import urllib.parse
import requests
import json

def get_requests(keyword):
    enc_keyword = urllib.parse.quote(keyword)
    query = "?term=" + enc_keyword + "&" + "media=music&entity=album&country=jp&lang=ja_jp"
    return requests.get("https://itunes.apple.com/search" + query).json()

def shape_json(result):
    return json.dumps(result, indent=2)
