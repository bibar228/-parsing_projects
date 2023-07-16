import requests
from bs4 import BeautifulSoup
import telebot

telega_token = "5926919919:AAFCHFocMt_pdnlAgDo-13wLe4h_tHO0-GE"
url = "https://funpay.com/"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
allNews = soup.findAll(class_='game-title')

games = []

for i in allNews:
    games.append(i.find("a").text)


with open("funpay-games.txt", "r+", encoding="UTF-8") as file:
    for i in file.readlines():
        if i.strip() not in games:
            chat_id = -695765690
            bot = telebot.TeleBot(telega_token)
            message = "Вышла новая игра - " + i
            bot.send_message(chat_id, message)
            file.write(i)
