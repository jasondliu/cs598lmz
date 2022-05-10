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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(2, my_cb, 0)

a = sqlite3.connect(DB_URI, uri=True)

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

my_threading_local.a = a

def test_fn(a, b):
    return a

def test_fn(a, b):
    return a

t = threading.Thread(target=test_fn, args=(1, 2))
t.start()
t.join()

# This should not segfault
a.execute("select test(1, 2)")
</code>

