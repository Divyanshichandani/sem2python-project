import requests

api_key='edb6ae89a778c60cfd8d6910b1099381'
city = input("Enter city: ")



def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    return response.json()

weather_data = get_weather_data(city, api_key)

def parse_weather_data(weather_data):
    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        temperature = main_data["temp"] - 273.15 # Convert from Kelvin to Celsius
        humidity = main_data["humidity"]
        weather_desc = weather_data["weather"][0]["description"]
        return temperature, humidity, weather_desc
    else:
        return None

temperature, humidity, weather_desc = parse_weather_data(weather_data)

def convert_temperature(kelvin):
    celsius = kelvin - 273.15
    return round(celsius, 2)

def display_weather_forecast(t, h, wd):
    print(f"\nTemperature in {city}: {round(t, 2)}°C")
    print(f"Humidity in {city}: {h}%")
    print(f"Weather Description of {city}: {wd}")

display_weather_forecast(temperature, humidity, weather_desc)   




'''weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {city} is: {weather}")
    print(f"The temperature in {city} is: {temp}ºF")'''
