import ctypes
import ctypes.util
import threading
import sqlite3
from datetime import datetime
from time import sleep
import time
import os
import sys

# Global Variables
# ================

# Path to the .so file
_path = ctypes.util.find_library('c')

# Path to the .h file
_header = ctypes.util.find_library('c')

# Opening the shared object
_mod = ctypes.CDLL(_path)

# Opening the header file
_mod = ctypes.CDLL(_header)

# Creating the sqlite3 database
conn = sqlite3.connect('/home/pi/Desktop/data.db')
c = conn.cursor()

# Creating the table
c.execute('''CREATE TABLE IF NOT EXISTS data(
    time text,
    temperature real,
    humidity real
    )''')

# Closes the connection
def close():
    conn.close()

# Writes to the database
