#!/home/aafedotov/lpg_bot/lpg_bot/venv/bin/python3

import os

from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from dotenv import load_dotenv


load_dotenv()

updater = Updater(token=os.getenv('BOT_TOKEN'))
bot = Bot(token=os.getenv('BOT_TOKEN'))
chat_id = os.getenv('CHAT_ID')


def say_hi(update, context):
    chat = update.effective_chat
    to_send = update.message.text
    text = 'Привет, я Бот! ' + to_send
    context.bot.send_message(chat_id=chat.id, text=text)


def wake_up(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text='Спасибо, что включили меня')
    button = ReplyKeyboardMarkup([['/add_lpg']], resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id,
                             text='Спасибо, данные отправлены')


def add_lpg(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text='Введите цену пропана')
    price = None
    while not price:
        try:
            price = float(update.message.text)
        except Exception:
            context.bot.send_message(chat_id=chat.id,
                                     text='Некорректный ввод.')
    context.bot.send_message(chat_id=chat.id,
                             text='Введите количество литров')
    value = None
    while not price:
        try:
            value = float(update.message.text)
        except Exception:
            context.bot.send_message(chat_id=chat.id,
                                     text='Некорректный ввод.')
    context.bot.send_message(chat_id=chat.id,
                             text=f'Вы ввели:{price} {value}')


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(CommandHandler('add_lpg', add_lpg))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.start_polling()
updater.idle()
