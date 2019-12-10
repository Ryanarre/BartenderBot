import telebot
from telebot import types
import sqlite3

start_text = 'Начать работу'
TOKEN = '1018546750:AAHcK_ANa0cyGUMuKKUvTLePhxedDWMTJTA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_action(message):
    start_menu = types.ReplyKeyboardMarkup(True, False)
    start_menu.row(start_text)

    bot.send_message(message.chat.id, 'Добро пожаловать в твой бар!', reply_markup=start_menu)

@bot.message_handler(content_types=['text'])
def main_action(message):
    if message.text == start_text:
        conn = sqlite3.connect('bartender.db')
        cursor = conn.cursor()
        question = cursor.execute('SELECT * FROM coctails ORDER BY RANDOM() LIMIT 1')

        response = cursor.fetchone()
        photo = open('./res/' + response[2] + '.png' , 'rb')
        '''bot.send_message(message.chat.id, cursor.fetchone()[0])'''
        bot.send_photo(message.chat.id, photo, response[1])

bot.polling();