import requests
import json
from datetime import datetime
import smtplib

#----------------------------------------------------------Email---------------------------------------------------#

my_mail = "cccccxxxxxxxx@gmail.com"
password = "xxxxxxxxxxxxxxxxxx"

def notify_user(msg):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        
        # Encode the message using UTF-8
        encoded_msg = msg.encode('utf-8')
        
        connection.sendmail(
            from_addr=my_mail, 
            to_addrs="xxxxxxxxxx@outlook.com", 
            msg=encoded_msg
        )

#--------------------------------------------------------Weather API--------------------------------------------------#

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'

weather_params = {
    "lat": 23.810331,
    "lon": 90.412521,
    "appid": api_key,
    "units": "metric"  # Request temperature in Celsius
}



response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()

# Extract relevant weather information (for example: temperature, weather description)
relevant_weather_info = {
    "temperature": weather_data["main"]["temp"],
    "feels_like": weather_data["main"]["feels_like"],
    "humidity": weather_data["main"]["humidity"],
    "description": weather_data["weather"][0]["description"]
}


#-----------------------------------------------------Time---------------------------------------------------#
time_now = str(datetime.now().time())

time_now = int(time_now.split(":")[0])



msg = ""
if time_now == 16:
    if relevant_weather_info["humidity"] >= 60 and relevant_weather_info["temperature"] >= 30:
        msg = "It's hot and humid outside! Please make sure to wear light clothes and drink plenty of water."
    elif relevant_weather_info["humidity"] >= 60 and relevant_weather_info["temperature"] < 30:
        msg = "It's humid outside! It might rain later today, so please have an umbrella with you."
    elif relevant_weather_info["humidity"] < 40 and relevant_weather_info["temperature"] < 20:
        msg = "It's cold outside! Please make sure to wear warm clothes."

notify_user(f"Subject: Daily Weather Alert\n\nDear Rehan, Good Morning! \nWeather is {relevant_weather_info['description']} \nTemperature: {relevant_weather_info['temperature']}°C \nFeels like: {relevant_weather_info['feels_like']}°C \nHumidity: {relevant_weather_info['humidity']} \n{msg}")

print(relevant_weather_info["description"])
print(relevant_weather_info['feels_like'])
print(relevant_weather_info['humidity'])

