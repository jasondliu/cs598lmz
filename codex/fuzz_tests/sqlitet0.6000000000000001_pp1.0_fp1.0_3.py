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
    a = my_threading_local.a
    a.execute("SELECT test(1, 2)")
    a.execute("SELECT test(1, 2)")
    return 1

def my_cb3(p):
    a = my_threading_local.a
    a.execute("SELECT test(1, 2)")
    a.execute("SELECT test(1, 2)")
    return 1

test_lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
test_lib.sqlite3_enable_shared_cache(1)

test_lib.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(ctypes.c_void_p()), 1, None)

thread_a = threading.Thread(target=my_cb)
thread_b = threading.Thread(target=my_cb2)
thread_c = threading.Thread(target=my_cb3)

thread_a.start()
