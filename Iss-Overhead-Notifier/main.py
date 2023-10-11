import requests
from datetime import datetime
import pytz
import smtplib
import time

my_mail = "XXXXXXX@gmail.com"
password = "XXXXXXXXXXXXXXXXXX"

MY_LAT = 23.707310 # Your latitude
MY_LONG = 90.415482 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data_iss = response.json()

iss_latitude = float(data_iss["iss_position"]["latitude"])
iss_longitude = float(data_iss["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def utc_to_bdt(utc_time):
    sum = int(utc_time)
    for i in range(6):
        if sum == 23:
            sum = -1
        sum += 1
    return sum


def notify_user(msg):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail, 
            to_addrs="XXXXXXXXX@outlook.com", 
            msg=msg
        )

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data_sun = response.json()
sunrise = utc_to_bdt(int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0]))
sunset = utc_to_bdt(int(data_sun["results"]["sunset"].split("T")[1].split(":")[0]))

time_now = str(datetime.now().time())

time_now = int(time_now.split(":")[0])

latitude_distance = abs(MY_LAT - iss_latitude)
longitude_distance = abs(MY_LONG - iss_longitude)


def is_iss_visible():
    if latitude_distance == float(5) and longitude_distance == float(5):
        if time_now <= sunrise or time_now >= sunset:
            notify_user("Subject: ISS is Visible Now!\n\nDear User, ISS is now visible in your local sky. Please look up.")


    notify_user("Subject: ISS is Not Visible Right Now\n\nDear User, ISS is now NOT visible in your local sky.")

while True:
    time.sleep(5)
    is_iss_visible()

