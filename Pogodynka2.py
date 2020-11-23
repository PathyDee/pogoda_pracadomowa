import requests
import re
from htmldom import htmldom

class Weather:
    def __init__(self, t, w, p):    #t = temperature, w = wind, p = pressure
        self.t = t
        self.w = w
        self.p = p

    def __add__(self, other):
        return Weather(self.t + other.t, self.w + other.w, self.p + other.p)

    def __truediv__(self, divider):
        return Weather(self.t / divider, self.w / divider, self.p / divider)

url_1 = "https://pogoda.onet.pl/prognoza-pogody/warszawa-357732"
site_1 = requests.get(url_1)
dom_1 = htmldom.HtmlDom().createDom(site_1.text)

Temp_onet = dom_1.find(".mainBoxContent").children(".mainParams").children(".temperature").children(".temp").text()
Temp_onet = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", Temp_onet)

###

url_2 = "https://pogoda.interia.pl/prognoza-dlugoterminowa-warszawa,cId,36917"
site_2 = requests.get(url_2)
dom_2 = htmldom.HtmlDom().createDom(site_2.text)

Temp_interia = dom_2.find(".weather-currently-middle-today-wrapper").children(".weather-currently-middle-today").children(".weather-currently-temp").text()
Temp_interia = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", Temp_interia)

###

url_3 = "https://pl.meteox.com/pl-pl/forecastlocation/d/4819858/warsaw"
site_3 = requests.get(url_3)
dom_3 = htmldom.HtmlDom().createDom(site_3.text)

Temp_meteox = dom_3.find(".forecast-type").children(".weathernow").children(".tempmax").text()
Temp_meteox = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", Temp_meteox)


#+ placeholdery dla wiatru i cisnienia
x_1 = float(Temp_onet[0])
x_2 = -1
x_3 = 999

y_1 = float(Temp_interia[0])
y_2 = 0
y_3 = 1000

z_1 = float(Temp_meteox[0])
z_2 = 1
z_3 = 1001


W1 = Weather(x_1, x_2, x_3)
W2 = Weather(y_1, y_2, y_3)
W3 = Weather(z_1, z_2, z_3)

WS = (W1 + W2 + W3)
WA = WS / 3

def pogodynka():
    print("###\nPogoda na dzisiaj:\ntemperatura: {}\nwiatr (placeholder): {}\nciśnienie (placeholder): {}\n###".format(WA.t, WA.w, WA.p))

pogodynka()