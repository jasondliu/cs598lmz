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

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        my_threading_local.a.execute("select test(1, 2)")

sqlite3.sqlite3_initialize()

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_threadsafe()

my_cb(None)

for i in range(0, 100):
    t = MyThread()
    t.start()

a = my_threading_local.a

a.execute("select test(1, 2)")

