import requests


api_key = "359d9f5c504e87b74fb6d75034fdb49f"
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
weather_params = {
    "lat": 48.751911,
    "lon": -122.478683,
    "appid": api_key
}
response = requests.get(OWM_Endpoint, weather_params)
print(response.status_code)
