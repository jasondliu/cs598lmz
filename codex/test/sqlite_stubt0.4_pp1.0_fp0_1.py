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

def my_cb2(p):
    my_threading_local.a.close()
    return 1

def test_threading():
    # load the sqlite3 extension
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_shared_cache(1)

    # register our threading callbacks
    lib.sqlite3_config(ctypes.c_int(7), my_cb, my_cb2)

    # create a connection
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    # create a thread
    t = threading.Thread(target=lambda: a.execute("select test(1, 2)"))
    t.start()
    t.join()

    # close the connection
    a.close()
