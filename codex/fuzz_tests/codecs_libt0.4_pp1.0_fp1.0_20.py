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

line_bot_api = LineBotApi('DVq3vq8gjY0p9XoH+xq3hb5z1g4l0b4w2BtJvB0DkR+dPXxnxVzg1i8y2OcZj+wZ1EkpvY8ZPYd+X9nxFxhQkzD8yQm5+a/wZm+mZhY/ZaS5X9x/e+3qcg/5z5/4b4+M2dJtBZDtRZ
