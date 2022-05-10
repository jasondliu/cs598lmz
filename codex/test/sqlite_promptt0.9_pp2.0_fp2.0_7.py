import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db").execute("CREATE TABLE t (c1 int, c2 int, c3 int);")
# Test sqlite3.connect("test.db").execute("CREATE INDEX t_c1 on t (c1);")
# Test print dict(sqlite3.connect("test.db").execute("PRAGMA index_info('t_c1')").fetchall())
# Test print dict(sqlite3.connect("test.db").execute("PRAGMA index_list('t')").fetchall())

_thread = ctypes.pythonapi._PyThreadState_Current
_thread.restype = ctypes.py_object
_thread.argtypes = ()

_all_threads = set()

def get_current_thread_id():
	return hex(ctypes.pythonapi.PyThread_get_thread_ident())

class sqlite3_threading(object):
	def __init__(self):
		self.lock = threading.Lock()

	def sqlite3_threading_simple_id(self):
		return get_
