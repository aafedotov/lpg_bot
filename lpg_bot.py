import os

from telegram import Bot
from dotenv import load_dotenv


load_dotenv()




bot = Bot(token=os.getenv('BOT_TOKEN'))
chat_id = os.getenv('CHAT_ID')
text = 'Hello, world!'
bot.send_message(chat_id, text)
