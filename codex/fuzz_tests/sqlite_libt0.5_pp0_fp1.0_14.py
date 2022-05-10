import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import json
import sys

# This is a test to try out sqlite3 and python
# The goal is to use a database to store the information from the keyboard
# The database will be used to store keystrokes, timestamp, process name
# and window title
#
# The database will be created in the current directory

# TODO:
# - Get the process name and window title
# - Create a database
# - Create a table for the keylogger
# - Insert the data into the table
# - Create a way to stop the keylogger
# - Create a way to start the keylogger
# - Create a way to send the data to a server
# - Create a way to receive the data from the server
# - Create a way to decrypt the data
# - Create a way to encrypt the data

# Create a database
#db = sqlite3.connect('keylogger.db')
#cursor = db.cursor()
#cursor.execute('''CREATE TABLE keylogger(timestamp TEXT, key TEXT, process TEXT, window_title TEXT)''')
