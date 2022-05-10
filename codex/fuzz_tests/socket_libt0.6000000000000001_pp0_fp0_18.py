import socket
import ssl
import sys
import threading
import time

from flask import Flask, request, jsonify

from . import get_logger
from .config import Config
from .database import Database
from .utils import Message, MessageType

logger = get_logger(__name__)

app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/v1/messages')
def get_messages():
    return jsonify([message.to_dict() for message in database.get_messages()])


@app.route('/api/v1/messages', methods=['POST'])
def post_message():
    message = Message(
        message=request.form['message'],
        username=request.form['username'],
        type=MessageType.text
    )
    database.add_message(message)
    return '', 204


class Client
