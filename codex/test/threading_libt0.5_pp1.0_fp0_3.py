import threading
threading.stack_size(67108864)

from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit

from threading import Thread
from time import sleep
from random import randint
from datetime import datetime

from game_engine import GameEngine

# Game settings
game_settings = {
    'grid_size': 20,
    'snake_length': 5,
    'food_count': 1,
    'food_points': 10,
    'game_speed': 0.5
}

# Game engine
game_engine = GameEngine(game_settings)

# Game state
game_state = {
    'players': [],
    'game_over': False,
    'game_start': False
}

# Flask
app = Flask(__name__)
app.secret_key = 'secret!'
socketio = SocketIO(app)

# Threads
game_thread = Thread()

# Helper functions
def background_thread():
    """Example of how to send server generated events to clients."""

