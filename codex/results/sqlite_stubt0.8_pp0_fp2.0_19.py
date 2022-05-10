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

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(0x0, 1, None)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.set_progress_handler(my_cb, 0)

# NOTE: This is different from the original test. Originally, the
# goal was to call a.create_function("test", 2, test_fn) prior to
# a.set_progress_handler, but that causes segfaults in Python 3.5,
# 3.6, and 3.7, so I use the progress handler to set up the callback
# function instead.
a.execute("SELECT test(7, ?);", (8,))
