import requests
from prettytable import PrettyTable
def getCovid(country):
    data = requests.get("https://api.covid19api.com/summary")
    json = data.json()
    l = json["Countries"]
    tb = PrettyTable(["Country","TotalConfirmed","TotalDeaths"])
    choose = 0
    if country  == "all":
        choose = 1
    for i in l:
        if choose == 0:
            if i["CountryCode"] == country:
                #print("Country\tTotalConfirmed\tTotalDeaths")
                tb.add_row([i["Country"],i["TotalConfirmed"],i["TotalDeaths"]])
                return tb
                #print("{}\t{}\t{}".format(i["Country"],i["TotalConfirmed"],i["TotalDeaths"]))
                break
        else: 
            tb.add_row([i["Country"],i["TotalConfirmed"],i["TotalDeaths"]])
    return tb
if __name__ == "__main__":
    tb = getCovid("VN")
    print(tb)

