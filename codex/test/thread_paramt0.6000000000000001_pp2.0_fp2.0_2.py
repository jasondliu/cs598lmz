import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from webdriver_manager.chrome import ChromeDriverManager

from config import *

# Define bot
bot = Bot(token=token)
updater = Updater(token=token, use_context=True)

# Define dispatcher
dispatcher = updater.dispatcher

# Define driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Define message
message = ''

def echo(update, context):
    print(f'{update.message.from_user.username}: {update.message.text}')
