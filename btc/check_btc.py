import requests
from bs4 import BeautifulSoup
import telebot

telega_token = "5926919919:AAFCHFocMt_pdnlAgDo-13wLe4h_tHO0-GE"
url = "https://www.rbc.ru/crypto/currency/btcusd?ysclid=lk9mbuvbs7343745173"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
allNews = soup.find(class_='chart__subtitle js-chart-value')



chat_id = -695765690
bot = telebot.TeleBot(telega_token)
message = "Цена битка - " + allNews.text.strip()[:6] + "$"
bot.send_message(chat_id, message)
