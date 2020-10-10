# Import modules
import telebot
from telebot import types

from sql import get_token, add_user
from SMS import FloodSMS

# Basic spam settings
SETTINGS = {
    "duration": 300,
    'threads_count': 6
}

# Bot initialization
bot = telebot.AsyncTeleBot(get_token())

# Start message
@bot.message_handler(commands=["start"])
def start(message):
    add_user(message.chat.username, message.chat.id)
    bot.send_message(message.chat.id, "Привет! Я бот который спамит SMS!😏\nОтправляй мне номер телефона и я все сделаю!👊\nНомер должен быть в таких форматах: +74992165050, 74992165050, 84992165050\nСейчас я туда отправлю кучу подарочков😋\n\nЕсли есть какие то вопросы или сомнения то напиши /faq")

# Initialization SMSSpam class
floodsms = FloodSMS(duration=SETTINGS["duration"], threads_count=SETTINGS['threads_count'])

# Get phone number
@bot.message_handler(regexp=r"\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b")
def phone(message):
    if floodsms.is_ranning == False:
        bot.send_message(message.chat.id, "Спам начался и будет длиться {} с. Чтобы остановить это все дело напиши /stop".format(SETTINGS['duration']))
        floodsms.run(phone=message.text)
    else:
        bot.send_message(message.chat.id, "Нее, сразу два номера нельзя!😡 Я останавливаю спам! Чтобы начать заного снова пришли мне номер")
        floodsms.stop()


# Stop spam
@bot.message_handler(commands=["stop"])
def stop(message):
    if floodsms.is_ranning:
        floodsms.stop()
        bot.send_message(message.chat.id, "Окей мы останавливаемся!\nЕсли хочешь еще присылай номер телефона😝")
    else:
        bot.send_message(message.chat.id, "А мне нечего останавливать🤷‍♂️")


# All message 
@bot.message_handler(content_types=["text", "sticker", "photo", "audio"])
def all_messages(message):
    bot.send_message(message.chat.id, "Так, я не понял что ты мне отправил. Напиши мне просто номер телефона😋")


if __name__ == "__main__":
    bot.polling()