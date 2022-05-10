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

static = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
static.sqlite3_shutdown.argtypes = None
static.sqlite3_shutdown.restype = None
static.sqlite3_initialize.argtypes = None
static.sqlite3_initialize.restype = None

DB = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
DB.create_function("init_db", 0, my_cb)

static.sqlite3_shutdown()
static.sqlite3_initialize()

#print(static.sqlite3_shutdown)
#print(static.sqlite3_initialize)

#DB.create_function("init_db", 0, my_cb)
#print("Hello World")
