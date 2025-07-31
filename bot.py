import telebot
from telebot import types
import csv
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['anketa'])
def ask_name(message):
    bot.send_message(message.chat.id, "Ismingizni kiriting:")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    name = message.text
    bot.send_message(message.chat.id, "Yoshingizni kiriting:")
    bot.register_next_step_handler(message, get_age, name)

def get_age(message, name):
    age = message.text
    user_id = message.from_user.id
    username = message.from_user.username or "yo'q"

    # CSV faylga yozamiz
    with open("foydalanuvchilar.csv", mode="a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, username, name, age])

    bot.send_message(message.chat.id, f"Rahmat, {name}! Ma’lumotlaringiz saqlandi.")

if __name__ == "__main__":
    print("Bot ishga tushdi!")
    bot.polling(none_stop=True)