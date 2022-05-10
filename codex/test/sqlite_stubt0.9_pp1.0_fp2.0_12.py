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

    return 10

def my_cb_fuzz():
    my_cb(None)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_config(5, 1)  # Configure the number of threads, needed?
lib.sqlite3_config(12, 1) # Configure the thread pool size
lib.sqlite3_initialize()  # Needed to start the thread pool

lib.sqlite3_config(45, ctypes.cast(my_cb_fuzz, ctypes.c_void_p))

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

a.create_function("whatever", 1, my_cb)

a.execute("select whatever(1) from sqlite_master;")
a.execute("select test(1, 2);")
