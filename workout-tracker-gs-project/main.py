from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

# Loading all the enviormental secrets
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")


APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

AUTHORIZATION = os.getenv("AUTH")

excerise_text = input("Enter the exercises you have performed: ")


excerise = {
    "query": excerise_text,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE,
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}


excerise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=excerise_endpoint, json=excerise, headers=header)
calories_data = response.json()

# Getting the various data required through json parsing
type_excerise = calories_data['exercises'][0]['name'].title()

calories_burnt = calories_data["exercises"][0]['nf_calories']

exerise_duration = (calories_data["exercises"][0]['duration_min'])



sheets_endpoint = "https://api.sheety.co/25fddd07859d2666aebf5de29336aa50/trackWorkouts/workouts"

sheets_header = {
    "Authorization" : AUTHORIZATION,
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Looping through each exercise
for exercise in calories_data['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            'exercise': type_excerise,
            'duration': exerise_duration,
            'calories': calories_burnt,
        }
    }
    # Posting the exercise to sheety and inturn passing it to my google sheets
    sheet_response = requests.post(url=sheets_endpoint, json=sheet_inputs)

    print(sheet_response.text)