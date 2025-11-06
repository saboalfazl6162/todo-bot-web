from balethon import Client,conditions
from dotenv import load_dotenv
import os

load_dotenv('.env')

bot = Client(os.getenv('BOT_TOKEN'))


bot.run()