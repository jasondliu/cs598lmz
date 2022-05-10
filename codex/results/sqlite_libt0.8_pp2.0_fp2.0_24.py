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

		try:
			_debug_msg = proto.DebugMessage()
			_debug_msg.module = _module
			_debug_msg.msg = _msg % args
			_debug_msg.time_stamp = time.time()
			_debug_msg.thread_id = threading.current_thread().ident
			_debug_msg.proc_id = os.getpid()

			_cursor = self.db.cursor()
			_cursor.execute('insert into debug_
