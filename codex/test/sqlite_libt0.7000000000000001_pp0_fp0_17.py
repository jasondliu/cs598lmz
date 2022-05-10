import ctypes
import ctypes.util
import threading
import sqlite3
import sys
from queue import Queue
from queue import Empty
from queue import Full
import paho.mqtt.client as mqtt
import time
import datetime

libc = ctypes.CDLL(ctypes.util.find_library('c'))

class Display():
	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.mqtt_client = mqtt.Client()
		self.mqtt_client.connect("localhost", 1883, 60)

		self.db_conn = sqlite3.connect("display.db")
		self.db_cursor = self.db_conn.cursor()
		self.db_cursor.execute("CREATE TABLE IF NOT EXISTS tickers (id INTEGER PRIMARY KEY, ticker TEXT, active INTEGER)")
		self.db_cursor.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, event TEXT, active INTEGER)")

