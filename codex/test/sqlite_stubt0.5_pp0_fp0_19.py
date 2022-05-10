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

def main():
    # find sqlite3.dll
    sqlite3_lib = ctypes.util.find_library("sqlite3")
    if sqlite3_lib is None:
        raise Exception("Could not find sqlite3.dll")

    # load the library
    sqlite3_lib = ctypes.CDLL(sqlite3_lib)

    # set up the callback
    my_cb_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    sqlite3_lib.sqlite3_config(ctypes.c_int(1), my_cb_c, ctypes.c_void_p(0))

    # start a thread
    thread = threading.Thread(target=lambda: sqlite3.connect(DB_URI, uri=True))
    thread.start()
    thread.join()

    # create a connection
    conn = sqlite3.connect(DB_URI, uri=True)
