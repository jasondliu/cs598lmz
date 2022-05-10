import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
import os
import sys
import traceback
import atexit

# For libtcc. See README.markdown.
try:
	from tcc import *
except:
	print("Could not import the libtcc module.\nthe libtcc module is required in order to compile the user code.")
	exit()

# For the watchdog thread.
import time

# For indexing the cookie jar and serving it to the user.
import random
import string
import urllib

class CookieJar:
	def __init__(self):
		self.jar = {}
		self.lock = threading.Lock()

	def set(self, key, val):
		self.lock.acquire()
		self.jar[key] = str(val)
		self.lock.release()

	def get(self, key):
		self.lock.acquire()
		val = self.jar[key]
		self.lock.release()
		return val

	def index(self):
		self.lock
