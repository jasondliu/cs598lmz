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

def test_fn(a, b):
    return a

def my_cb_thread(p):
    try:
        my_cb(p)
    except:
        pass

def my_cb_thread_2(p):
    try:
        my_cb(p)
    except:
        pass

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_shared_cache(1)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.create_function("test", 2, test_fn)

    lib.sqlite3_config(1, my_cb, None)

    t = threading.Thread(target=my_cb_thread, args=(None,))
    t.start()
    t.join()

    t = threading.Thread(target=my_cb_thread_2, args=(None,))
    t.start()
    t.join()

    my
