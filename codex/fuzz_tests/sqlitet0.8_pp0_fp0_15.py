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

#attempt to open a connection during a callback
sqlite3.load_extension("test", "test")
sqlite3.create_function("test", 1, my_cb)
sqlite3.enable_callback_tracebacks(True)
sqlite3.complete_statement("select test(1)")
