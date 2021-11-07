import requests
from bs4 import BeautifulSoup
import csv

HOST = "https://stopgame.ru/"
URL = "https://stopgame.ru/news/"
HEADERS = {
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,im    age/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

def get_html(url,params= ""):
    r = requests.get(url,headers = HEADERS,params = params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="item article-summary")
    blox = []
    
    for item in items:
        blox.append(
            {
                "title": item.find("div" , class_ ="caption caption-bold").get_text(),
                "link_blok": item.find("div" , class_ ="caption caption-bold").find("a").get("href"),
                "img_blok": item.find("a" , class_ ="article-image").find("img").get("src")
            }
        )
    return blox

html = get_html(URL)
print(get_content(html.text))