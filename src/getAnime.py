import requests
from bs4 import BeautifulSoup
def getListAnime(year):
    url = f"https://animehay.tv/phim-phat-hanh/{year}?page=1"
    resp = requests.get(url)
    jsoup = BeautifulSoup(resp.content,"html.parser")
    ls = jsoup.find_all("div",{"class":"ah-pad-film"})
    url_list = []
    for i in ls:
        url_list.append(i.find("a").get("href"))
    return url_list
if __name__ == "__main__":
    ls = getListAnime("2021")
    print(ls)
