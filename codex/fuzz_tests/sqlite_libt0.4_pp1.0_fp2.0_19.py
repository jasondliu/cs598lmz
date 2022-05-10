import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time

from libmumble import *

if sys.platform == "win32":
	import _winreg
	import win32api
	import win32con
	import win32gui
	import win32process
	import win32security
	import win32ts

class MumbleServer(object):
	def __init__(self, name, address, port, username, password):
		self.name = name
		self.address = address
		self.port = port
		self.username = username
		self.password = password
		self.is_connected = False

	def connect(self):
		if self.is_connected:
			return

		self.is_connected = True
		self.thread = threading.Thread(target=self.connect_thread)
		self.thread.start()

	def connect_thread(self):
		mumble = Mumble(self.address, self.port, self.username, self.password)
		mumble.start()
		m
