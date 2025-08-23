from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

MY_LAT = 18.61
MY_LONG = 73.74

load_dotenv()

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": os.getenv("TWILIO_APP_ID"),
    "cnt": 4
}

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
message_sid = os.getenv("MESSAGE_SID")
TO_NUMBER = os.getenv("TO_NUMBER")

id_codes = []

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for i in range(0,4):
    code = weather_data["list"][i]['weather'][0]['id']
    if int(code) < 700:
        will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid=message_sid,
        body="It's going to rain today, Remember to bring an ☔",
        to=TO_NUMBER
    )
    print(message.status)