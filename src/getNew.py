from bs4 import BeautifulSoup
import requests
def getURL():
    url_list = []
    url = 'https://baomoi.com/'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content,'html.parser')
    ls = soup.find_all("div",{"class":"bm_AP"})
    for i in ls:
        url_list.append(url+i.next_element.next_element.next_element.next_element.get('href'))
    return url_list
if __name__ == "__main__":
    ls = getURL()
    for i in ls:
        print(i)
