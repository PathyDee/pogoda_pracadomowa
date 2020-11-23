import requests
import re
from htmldom import htmldom

site_url = "https://pogoda.onet.pl/prognoza-pogody/warszawa-357732"
response = requests.get(site_url)
dom = htmldom.HtmlDom().createDom(response.text)

Temp_onet = dom.find(".mainBoxContent").children(".mainParams").children(".temperature").children(".temp").text()
Temp_onet = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", Temp_onet)

###

site_url = "https://pogoda.interia.pl/prognoza-dlugoterminowa-warszawa,cId,36917"
response = requests.get(site_url)
dom = htmldom.HtmlDom().createDom(response.text)

Temp_interia = dom.find(".weather-currently-middle-today-wrapper").children(".weather-currently-middle-today").children(".weather-currently-temp").text()
Temp_interia = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", Temp_interia)

###

site_url = "https://pl.meteox.com/pl-pl/forecastlocation/d/4819858/warsaw"
response = requests.get(site_url)
dom = htmldom.HtmlDom().createDom(response.text)

Temp_meteox = dom.find(".forecast-type").children(".weathernow").children(".tempmax").text()
Temp_meteox = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", Temp_meteox)

###

Temp_srednia = ((float(Temp_onet[0])) + (float(Temp_interia[0])) + (float(Temp_meteox[0]))) / 3
print("Średnia temparatura dzisiaj wynosi: " + str(Temp_srednia))