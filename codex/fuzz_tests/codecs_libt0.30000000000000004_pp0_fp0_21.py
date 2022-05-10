import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

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

line_bot_api = LineBotApi('p5g5BV7gH+xF9V9YzZ+QJZ7DzHb5PV7+8FbQ1QQHd+iJXKj8YmWtZv7w1kHjGzJ/1q3G4+/Kjfz0sX9Y8/NjPvBwJjB/C0QqG3q4q4yjKxJiXBXn8bZSj7ZzwKj1Qn2Q8eWcQy2d0
