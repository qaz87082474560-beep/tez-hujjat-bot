import telebot
from flask import Flask
import threading
import os

TOKEN = "8654475059:AAHjZD5cZAe-JWcTZzKzjQvutEq4yNOYGTg"  # BotFather берган token

bot = telebot.TeleBot(TOKEN)

# --- BOT LOGIC ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom 👋 Bot ishlayapti!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, "Siz yozdingiz: " + message.text)


# --- FLASK (KEEP ALIVE) ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti"

def run_web():
    app.run(host='0.0.0.0', port=8080)


# --- RUN ---
if __name__ == "__main__":
    # web serverni alohida threadda ishga tushuramiz
    threading.Thread(target=run_web).start()

    print("Bot ishga tushdi...")
    bot.infinity_polling()
