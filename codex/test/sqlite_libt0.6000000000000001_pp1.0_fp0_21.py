import ctypes
import ctypes.util
import threading
import sqlite3
import sys

# TODO: 
# - add a timeout to the acquireLock() method, so that lock acquisition can't hang the program
# - add some kind of locking to the getFileSize() method, so that multiple threads don't try to
#   update the size of the same file at once

# This class is a wrapper around the sqlite3 database used to store the cache.
class CacheDB:
	_db_lock = threading.Lock()

	def __init__(self, path):
		self.db = sqlite3.connect(path)
		self.db.text_factory = str
		c = self.db.cursor()
		c.execute('CREATE TABLE IF NOT EXISTS files (path TEXT PRIMARY KEY, size INTEGER, timestamp INTEGER)')
		c.execute('CREATE TABLE IF NOT EXISTS locks (path TEXT PRIMARY KEY, lock INTEGER)')
		self.db.commit()

	# Acquire an exclusive lock on the given file. Will block until the lock is acquired.
