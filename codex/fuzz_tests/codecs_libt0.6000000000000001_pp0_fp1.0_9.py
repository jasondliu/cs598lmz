import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import os
from flask import Flask, request, abort
import json
import requests
from datetime import datetime
import csv

app = Flask(__name__)

line_secret = os.environ["LINE_CHANNEL_SECRET"]
line_access_token = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

# 環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line
