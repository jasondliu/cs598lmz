import ctypes
import ctypes.util
import threading
import sqlite3

from . import config
from . import paths

class Database(object):
	def __init__(self):
		self.db = None
		self.lock = threading.Lock()

	def __del__(self):
		if self.db is not None:
			self.db.close()

	def _open(self):
		if self.db is None:
			self.lock.acquire()
			try:
				if self.db is None:
					self.db = sqlite3.connect(paths.get_db_file())
			finally:
				self.lock.release()

	def _close(self):
		if self.db is not None:
			self.lock.acquire()
			try:
				if self.db is not None:
					self.db.close()
					self.db = None
			finally:
				self.lock.
