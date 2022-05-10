import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os

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

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('DlU6lwU2QJy0jazvY7X9Yz+cV7xE6LZuVQ4+q3q4V
