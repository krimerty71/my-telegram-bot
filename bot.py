import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")  # Токен хранится в переменной окружения

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Напиши /post.")

print("BOT STARTED")
bot.infinity_polling()
