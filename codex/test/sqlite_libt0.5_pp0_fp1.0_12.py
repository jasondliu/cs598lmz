import ctypes
import ctypes.util
import threading
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import os
import ast
import random

app = Flask(__name__)
socketio = SocketIO(app)
CORS(app)

# Global variables

# List of all the connected clients
clients = []

# List of all the available rooms
rooms = []

# List of all the messages
messages = []

# Dictionary to store the room name and the list of users in that room
room_users = {}

# Dictionary to store the username and the list of rooms the user is in
user_rooms = {}

# Dictionary to store the username and the list of messages the user has sent
user_messages = {}

# Dictionary to store the username and the list of messages the user has received
user_rec_messages = {}

# Dictionary to store the username and the list of messages the user has sent in a particular room
user_room_messages = {}

# Dictionary to store the
