import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import time

# Setup function
def setup():
	# Create database
	database = sqlite3.connect('/home/pi/Desktop/Database.db')
	cursor = database.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS Temperatures(DateTime TEXT, Temperature TEXT)''')
	database.close()

# Main function
def main():
	# Default values
	t = 0
	r = 0
	v = 0
	r2 = 0
	v2 = 0
	t2 = 0
	# Initialize library
	lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('wiringPi'))
	# Initialize pin 17 as an input
	lib.wiringPiSetupGpio()
	lib.pinMode(17, 0)
	# Initialize pin 18 as an input
	lib.wiringPiSetupGpio()
	lib.pinMode(18, 0)
	# While loop
