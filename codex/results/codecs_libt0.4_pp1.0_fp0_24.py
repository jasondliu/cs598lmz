import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys
import time
import json
import random
import requests
import datetime
import MySQLdb
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        text = msg['text']
        if text.startswith('/'):
            if text == '/start':
                bot.sendMessage(chat_id, 'Welcome to the bot!\n\n/help - show this message\n/random - generate a random number\n/post - post a random post from the database\n/post [id] - post a post from the database with the given id\n/post [id]-[id] - post a random post from the database between the given ids\n/post [id]-[id] [amount] - post a
