import requests
from prettytable import PrettyTable
def getWeather(city):
    city = city.replace("_","%20")
    #print(city)
    myKey = "e90072222e60645e2f9ed2949daec557"
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,myKey))
    json = data.json()
    weather = json["weather"]
    #print(weather[0]["description"])
    temp = json["main"]
    tb = PrettyTable(["city","description","temp"])
    tb.add_row([json["name"],weather[0]["description"],str(round(temp["temp"]/10,2))+u"\N{DEGREE SIGN}"+"C"])
    return tb
