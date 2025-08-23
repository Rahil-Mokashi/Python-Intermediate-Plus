from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

user_endpoint = "https://pixe.la/v1/users"

user_config = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : 'yes',
    "notMinor": 'yes',
}

response = requests.post(url=user_endpoint, json=user_config)

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

auth_header = {
    "X-USER-TOKEN": TOKEN, 
}

graph_config = {
    "id": GRAPH_ID,
    "name": 'Water Tracker',
    "unit": "liters",
    "type": "int",
    "color": "sora",
}


response = requests.post(url=graph_endpoint, json=graph_config, headers=auth_header)
print(response.text)


today = datetime.now()
date = today.strftime("%Y%m%d")

pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date": date,
    "quantity": "2",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=auth_header)
print(response.text)

update_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

update_config = {
    "quantity": "3"
}

response = requests.put(url=update_endpoint, json=update_config, headers=auth_header)
print(response.text)
