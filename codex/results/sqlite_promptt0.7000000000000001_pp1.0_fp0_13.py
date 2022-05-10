import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('sensors.db')
# Test sqlite3.connect('sensors.db').cursor().execute('CREATE TABLE sensors(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, value REAL)')
# Test sqlite3.connect('sensors.db').cursor().execute('INSERT INTO sensors (name, value) VALUES (?, ?)', ('temperature', 2))
# Test sqlite3.connect('sensors.db').cursor().execute('SELECT * FROM sensors')
# Test sqlite3.connect('sensors.db').cursor().fetchall()

# Load the library.
lib = ctypes.util.find_library('mraa')
if lib is None:
    raise Exception("Could not find mraa library")
mraa = ctypes.CDLL(lib)

# Call mraa_init().
mraa.mraa_init()

# Initialise the temperature sensor.
sensor = mraa.mraa_aio_init(0)

# Read the current temperature.
def read
