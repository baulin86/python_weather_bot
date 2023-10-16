from config import WTH_TOKEN as TOKEN
import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(latitude, longitude, lang):
    params = {'lat':latitude, 'lon':longitude, 'units':'metric', 
              'lang':lang, 'appid':TOKEN}
    
    response = requests.get(BASE_URL, params = params)
    data = response.json()
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    wind = data['wind']['speed']
    wind_deg = data['wind']['deg']
    icon = data['weather'][0]['icon']
    city = data['name']
    
    return description,temp,wind,city,icon,wind_deg

def get_coordinate(city):
    URL = 'http://api.openweathermap.org/geo/1.0/direct'
    
    params = {'q': city, 'limit': 5,'appid': TOKEN}
    response = requests.get(URL, params = params)
    data = response.json()
    if data:
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return latitude, longitude
    else:
        return false