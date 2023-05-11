import os
import requests

def handler(event, context):
    # Get the country code from the event
    country_code = event['country_code']
    
    # Build the URL for the weather API
    api_key = '3914cdab21e1815a5b0df8de2e174068'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={country_code}&appid={api_key}'
    
    # Call the weather API
    response = requests.get(url)
    data = response.json()
    
    # Parse the weather data
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    
    # Return the weather forecast
    return f'The weather in {country_code} today is {weather_description} with a temperature of {temperature} Kelvin.'
