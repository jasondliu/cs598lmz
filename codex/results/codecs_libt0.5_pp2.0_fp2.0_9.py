import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import random
from datetime import datetime
from datetime import timedelta

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('+yJ0Sf+Gvj8KWzGJX0gFZtTpTtL+fKF0JqC3yqJxvxKH+2cRtXlGtTmTtT+CKj/zsJmqh3xHmvj1Q+ZM9hZ4/4/j+vZ
