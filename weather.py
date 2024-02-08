import requests, json, functions

# pesquisa, cidade, país, estado, código postal
searchType = {"q","city","country","state","postalcode"}
city = "brasília"
format = "jsonv2"

local = requests.get(f"https://nominatim.openstreetmap.org/search.php?q={city}&format={format}")

data = json.loads(local.content)

latitude = data[0]["lat"]
longitude = data[0]["lon"]
localName = data[0]["display_name"]

weather = json.loads(requests.get(f"https://www.7timer.info/bin/astro.php?{longitude}&{latitude}&ac=0&unit=metric&output=json&tzshift=0").content)

forecastType = weather["product"]
timeForecast = f"{weather["init"][:4]}-{weather["init"][4:6]}-{weather["init"][6:8]}-{weather["init"][8:10]}"
clima = weather["dataseries"]

statusWeather = {
    "rain": "chuvoso",
    "none": "limpo"
}

def main():
    tabela = {}
    for i in clima:
        hourAdd = i["timepoint"]
        cloudPercent = i["cloudcover"]
        airDamp = i["rh2m"]
        windDirection = i["wind10m"]["direction"]
        windSpeed = i["wind10m"]["speed"]
        temperature = i["temp2m"]
        expectWeather = i["prec_type"]
        
        
        weatherTime = functions.translateTime(timeForecast, hourAdd)
        
        items = {
            "0": f"{cloudPercent * 10}% de nuvens no céu",
            "1": f"{airDamp}% de umidade relativa no ar",
            "2": f"Ventos de até {windSpeed * 3.6}Km/h, vindos do {functions.windDirection(windDirection)}",
            "3": f"Espera-se um dia {statusWeather.get(expectWeather, "Desconhecido")}, com temperatura de {temperature}°C."
        }
        
        tabela[weatherTime] = items
        
    return json.dumps(tabela, indent=4)
    
