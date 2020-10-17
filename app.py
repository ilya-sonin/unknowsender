# Import modules
import telebot
from telebot import types

from sql import get_token, add_user
from SMS import FloodSMS

messages = {
    "start": """Привет! Я бот который спамит СМС-ки!\nПросто отправляй мне номер телефона в любом формате, но с кодом страны""",
    "spam_start": """Спам начался и будеь длится {duration} с.\nЧтобы все остановить напиши /stop
    """,
    "spam_two_numbers": """Сразу два номер нельзя. Я останавливаю спам!
    """,
    "spam_stop": """
    Я останавливаюсь. Если хочешь присылай еще номер
    """,
}

# Basic spam settings
SETTINGS = {
    "duration": 300,
    'threads_count': 12
}

# Bot initialization
bot = telebot.AsyncTeleBot(get_token())

# Start message
@bot.message_handler(commands=["start"])
def start(message):
    add_user(message.chat.username, message.chat.id)
    bot.send_message(message.chat.id, messages["start"])

# Initialization SMSSpam class
floodsms = FloodSMS(duration=SETTINGS["duration"], threads_count=SETTINGS['threads_count'])

# Phone number
@bot.message_handler(regexp=r"(?:\+|\d)[\d\-\(\) ]{9,}\d")
def phone(message):
    if floodsms.is_ranning == False:
        bot.send_message(message.chat.id, messages["spam_start"].format(duration=SETTINGS['duration']))
        floodsms.run(phone=message.text)
    else:
        bot.send_message(message.chat.id, messages["spam_two_numbers"])
        floodsms.stop()

# Stop spam
@bot.message_handler(commands=["stop"])
def stop(message):
    if floodsms.is_ranning:
        floodsms.stop()
        bot.send_message(message.chat.id, messages["spam_stop"])
    else:
        bot.send_message(message.chat.id, "А мне нечего останавливать🤷‍♂️")


# All message 
@bot.message_handler(content_types=["text", "sticker", "photo", "audio"])
def all_messages(message):
    bot.send_message(message.chat.id, "Так, я не понял что ты мне отправил. Напиши мне просто номер телефона")


if __name__ == "__main__":
    bot.polling()