import telebot 
import sqlite3
import random 
import requests
from config import token
from telebot import types
bot = telebot.TeleBot(token)
con = sqlite3.connect("user.db")
cur = con.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        city TEXT
    )
''')
factors = []
countries = []
qviz_questions = []
@bot.message_handler(commands = ["start"])
def start_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width= 2)
    markup.add (types.InlineKeyboardButton("Факторы 🌍", callback_data='factors'))
    markup.add(types.InlineKeyboardButton("Страны 🌎", callback_data='countries'))
    markup.add(types.InlineKeyboardButton("Как себя вести 📋", callback_data='behavior'))
    markup.add(types.InlineKeyboardButton("Изменение температур 📈", callback_data='temperature'))
    markup.add(types.InlineKeyboardButton("Установить город 🏙️", callback_data='set_city'))
    markup.add(types.InlineKeyboardButton("Играть в викторину 🎯", callback_data='quiz'))
    bot.send_message(message.chat.id, "Привет! Я бот о глобальном потеплении.", reply_markup=markup)
@bot.callback_query_handler(func = lambda call:True)
def callback_qwery(call):
    if call.data == "factors":
        fact = random.choice(factors)
        bot.answer_callback_query(call.id, "Фактор выбран")
        bot.send_message(call.message.chat.id,f'Фактор глобального потепления: {fact}')
    elif call.data == "countries":
        text = "\n".join(countries)
        bot.send_message(call.chat.message.id, f"Страны с наибольшим потеплением {text}")
    elif call.data == "behavior":
        bot.send_message(call.message.chat.id,
                            "✅ Что делать:\n\n"
                            "- Экономить электричество\n"
                            "- Использовать велосипед\n"
                            "- Сократить потребление воды\n"
                            "- Сажать деревья\n"
                            "- Информировать других")
