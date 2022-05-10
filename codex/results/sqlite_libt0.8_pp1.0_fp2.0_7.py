import ctypes
import ctypes.util
import threading
import sqlite3
import os
from Queue import Queue
from time import sleep
from datetime import datetime
from time import sleep
from flask import Flask, render_template, request, g

# Set up our database for saving the information
DATABASE = '/home/pi/Desktop/DAUGHTERBOARD/DB/alarm_clock.db'

# Initialize the flask app
app = Flask(__name__)
app.config.from_object(__name__)

# Set up the queue for passing around events
event_queue = Queue()

# Function to create the database, if it doesn't already exist
def init_db():
    print "Creating the DB"
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as file:
            db.cursor().executescript(file.read())
        db.commit()

# Function to connect to the database
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    r
