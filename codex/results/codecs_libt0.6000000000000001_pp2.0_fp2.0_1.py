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

line_bot_api = LineBotApi('RZR+bI0D0w2QkvzKrOqrq3HqW5YiKjYXh4Z4j6LqVwUaD6gIe7mhS1AjV7c2mP9u/njZzTfTg/c8z1/nKj/yNhBKsAJ/DnYXZ4O6q3x6h0VwOuHpBhV7yjGgQdV7BXOvQZL0rxTlTcOl
