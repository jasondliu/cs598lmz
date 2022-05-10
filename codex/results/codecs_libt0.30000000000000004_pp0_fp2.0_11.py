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

app = Flask(__name__)

line_bot_api = LineBotApi('+WjE/J+0o/cq3qjmZ+1pYjYVtq+q3DnV7B1K5b5+7QnxnZuV7Zwg+Yzj7fJ9lHvVJk2jd+g4f4j4x4Z4hJw/E+mJ0V7+uQ2Z5V7zY1F3qV7o0XtjKV7LbP/4N4D4j1xwZ+8Y/Q2Sz
