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

def my_warning_cb(x, y):
    pass


if __name__ == "__main__":
    cdll.LoadLibrary(ctypes.util.find_library("c"))

    sqlite3.enable_callback_tracebacks(True)
    sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    sqlite3.set_progress_handler(my_cb, 1000)
    sqlite3.set_warning_handler(my_warning_cb)

    con = sqlite3.connect("file:test?mode=memory", uri=True, factory=deleting_conn)

    con.set_progress_handler(my_cb, 1000)
    con.set_warning_handler(my_warning_cb)

    con.create_function("test", 2, lambda a, b: a)

    my_threading_local.con = con

    print("DONE")
