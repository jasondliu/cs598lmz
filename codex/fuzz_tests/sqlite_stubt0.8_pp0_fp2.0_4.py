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

def test_threads():

    a = sqlite3.connect("file:test", uri=True)

    a.execute("create table test (x int)")
    a.execute("select sqlite3_initialize()")

    sqlite3.enable_callback_tracebacks(True)

    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    sqlite3_threading = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))

    sqlite3_threading.sqlite3_threadsafe()

    b.create_function("test", 1, my_cb)
    b.execute("select test(1)").fetchall()

    return True

try:
    test_threads()
except Exception as e:
    print(e)
