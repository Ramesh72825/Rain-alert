import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "67d27fc905249ef9de55f24d025ca221"

weather_params = {
    "lat": 26.920980,
    "long": 75.794220,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

