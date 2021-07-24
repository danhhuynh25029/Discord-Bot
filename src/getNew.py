from bs4 import BeautifulSoup
import requests
url = 'https://baomoi.com/'
resp = requests.get(url)
soup = BeautifulSoup(resp.content,'html.parser')
ls = soup.find_all("h4",{"class":"bm_P"})
for i in ls:
    print(i)
