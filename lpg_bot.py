import os

from telegram import Bot
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from dotenv import load_dotenv


load_dotenv()

updater = Updater(token=os.getenv('BOT_TOKEN'))
bot = Bot(token=os.getenv('BOT_TOKEN'))
chat_id = os.getenv('CHAT_ID')


def say_hi(update, context):
    chat = update.effective_chat
    print(update)
    context.bot.send_message(chat_id=chat.id, text='Привет, я Бот!')


def wake_up(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text='Спасибо, что включили меня')


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.start_polling()
updater.idle()
