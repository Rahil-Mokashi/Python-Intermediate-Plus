from dotenv import load_dotenv
import os
import requests
from newsapi import NewsApiClient
from twilio.rest import Client


load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
APP_ID = os.getenv("APP_ID")
NEWS_APP_ID = os.getenv("NEWS_APP_ID")
ACC_SID = os.getenv("ACC_SID")
TOKEN_NO = os.getenv("TOKEN_NO")
TWILIO_NO = os.getenv("TWILIO_NO")
TWILIO_WHAT_NO = os.getenv("TWILIO_WHAT_NO")
TO_NUMBER = os.getenv("TO_NUMBER")

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={APP_ID}'
r = requests.get(url)
data = r.json()

dates = list(data['Time Series (Daily)'].keys())

previous_day_close = float(data['Time Series (Daily)'][dates[1]]["4. close"])

day_before_close = float(data['Time Series (Daily)'][dates[2]]["4. close"])

fluctuation = int(((previous_day_close - day_before_close) / previous_day_close) * 100)

if(fluctuation>=5 or fluctuation<=-5):



    link = f"https://newsapi.org/v2/everything?q=Tesla%20Inc&from={dates[2]}&to={dates[1]}&sortBy=popularity&apiKey={NEWS_APP_ID}"
    news = requests.get(link)
    news_data = news.json()

    first_news_title = news_data["articles"][0]["title"]
    second_news_title = news_data["articles"][1]['title']
    third_news_title = news_data["articles"][2]['title']

    if (fluctuation > 5):
        message_text = f"TSLA: 🔺{fluctuation}\nHeadline1: {first_news_title}\n\nHeadline2: {second_news_title}\n\nHealine3: {third_news_title}"
    elif(fluctuation < 5):
         message_text = f"TSLA: 🔻{fluctuation}\nHeadline1: {first_news_title}\n\nHeadline2: {second_news_title}\n\nHealine3: {third_news_title}"

    client = Client(ACC_SID, TOKEN_NO)
    message = client.messages.create(
        from_= TWILIO_WHAT_NO,
        body=message_text,
        to= TO_NUMBER,
    )
    print(message.status)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  