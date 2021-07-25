import requests
def getCovid(country):
    data = requests.get("https://api.covid19api.com/summary")
    json = data.json()
    l = json["Countries"]
    tb = '''
    Country : {}
    TotalConfirmed : {}
    TotalDeaths : {}
    '''
    choose = 0
    ls = []
    if country  == "all":
        choose = 1
    for i in l:
        if choose == 0:
            if i["CountryCode"] == country:
                ls.append([i["CountryCode"],i["Country"],i["TotalConfirmed"],i["TotalDeaths"]])
                return ls
        else: 
            ls.append([i["CountryCode"],i["Country"],i["TotalConfirmed"],i["TotalDeaths"]])
    return ls
if __name__ == "__main__":
    tb = getCovid("US")
    t = tb[0]
    print(t[0])

