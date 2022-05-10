import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('m4JFT7V4mOo+L7+8KtJw1tEa+zYfZsB8cg2n1X9sCvH/y75WELCnLwIjTpTnDZfuYzp6Kj+6Xqn1U2n6aGJaPMU+RfUx+6iZ/Gp/zpA3I/qk1qG2lHWlNvdNU6l0U6NbO6zYsHfQGdzIeCKmIP67wdB04t89/1O/
