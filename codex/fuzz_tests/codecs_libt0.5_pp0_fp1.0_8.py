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

# Channel Access Token
line_bot_api = LineBotApi('i6H1z6mZgx/F6HWn6XFh6V1UyEgU6DpzB1KvZ7DzZG+eV7WL9aYvV7p+R5R5V8WwJlzv4fq3Qx4bM+1t9XBtqrq3dJyO/z+wJH0/0/pjxRJg0fIp9VeY+s7gJm+sLmT0T+2QT
