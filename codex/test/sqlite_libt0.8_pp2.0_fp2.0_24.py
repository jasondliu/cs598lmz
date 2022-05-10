import ctypes
import ctypes.util
import threading
import sqlite3
import pytz
import traceback
import logging

try:
	from urllib.parse import quote_plus
except ImportError:
	from urllib import quote_plus

import db
import messages_pb2 as proto

class DebugLogger:
	def __init__(self, _db):
		self.db = _db
		self.lock = threading.Lock()

	def log_debug(self, _module, _msg, *args):
		self.lock.acquire()

