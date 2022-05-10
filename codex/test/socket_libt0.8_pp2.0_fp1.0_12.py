import socket
from threading import Thread
from time import sleep

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect

from HistorianServer import HistorianServer
from PubSub import Publisher, Subscriber

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

thread = None

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


