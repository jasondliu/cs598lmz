import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time

# Define a class for the thread.
class ScanThread(threading.Thread):
	def __init__(self, threadName, filelist, database, connection, c_lib, c_lib_name):
		threading.Thread.__init__(self)
		self.threadName = threadName
		self.filelist = filelist
		self.database = database
		self.connection = connection
		self.c_lib = c_lib
		self.c_lib_name = c_lib_name
		self.file_count = 0
		
	def run(self):
		self.connection.execute('BEGIN TRANSACTION')
		self.connection.execute('PRAGMA synchronous = OFF')
		self.connection.execute('PRAGMA journal_mode = MEMORY')
		self.connection.execute('PRAGMA temp_store = MEMORY')
		self.connection.execute('PRAGMA cache_size = 20000')
