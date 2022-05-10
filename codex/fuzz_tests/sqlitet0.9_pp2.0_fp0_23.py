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

if __name__  == "__main__":

    dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    destroycallback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(my_cb)
    try:
        dll.sqlite3_subscriber_initialize()
    except AttributeError:
        dll.sqlite3_subscribe_initialize()

    dll.sqlite3_subscribe_events(ctypes.c_int(0), destroycallback, b"BEGIN;\000")
    dll.sqlite3_subscribe_events(ctypes.c_int(0), destroycallback, b"END;\000")
    dll.sqlite3_subscribe_events(ctypes.c_int(0), destroycallback, b"COMMIT;\000")
    dll.sqlite3_subscribe_events(ctypes.c_int(0), destroycallback, b"ROLLBACK;\000")

    p = sqlite
