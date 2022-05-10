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

library = ctypes.CDLL(ctypes.util.find_library(ctypes.util.libname("sqlite3")))

try:
    sqlite3.enable_callback_tracebacks(True)
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.create_function("my_cb", 0, my_cb)
    conn.close()
    library.sqlite3_enable_load_extension(sqlite3._sqlite3.dbapi2.sqlite3(), 1)
    library.sqlite3_load_extension(sqlite3._sqlite3.dbapi2.sqlite3(), "sqlite3_simpleext", "my_cb", 0)
    library.sqlite3_enable_load_extension(sqlite3._sqlite3.dbapi2.sqlite3(), 0)
except:
    print("Exception in main thread")

def thread_fn():
    try:
        conn = sqlite3.connect(DB_URI, uri=True)
        cursor = conn.cursor()
