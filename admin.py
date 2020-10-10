import telebot
from telebot import types

from sql import get_token, get_users_chat_ids

# Bot initialization
bot = telebot.TeleBot(get_token())
text = ""

for chat_id in get_users_chat_ids():
    try:    
        bot.send_message(chat_id, text)
    except telebot.apihelper.ApiTelegramException:
        pass

