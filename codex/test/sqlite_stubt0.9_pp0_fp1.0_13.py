import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def another_cb(p):
	a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

	def test_fn(a, b):
		return a

	a.create_function("test", 2, test_fn)

	my_threading_local.a = a

	return 1

def destroyable_cb(p):
	return 1

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))

class Conn(ctypes.Structure):
    pass

class Fake():
    def __del__(self):
        global lib
        p = ctypes.pointer(self.conn)
        lib.sqlite3_close(p)

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
