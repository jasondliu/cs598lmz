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
lib.sqlite3_enable_shared_cache(1)
lib.sqlite3_config(ctypes.c_int(10), my_cb, 0)

a = sqlite3.connect(DB_URI, uri=True)

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

my_threading_local.a = a

def worker():
    b = sqlite3.connect(DB_URI, uri=True)
    b.create_function("test", 2, test_fn)
    my_threading_local.b = b

t = threading.Thread(target=worker)
t.start()
t.join()

a.execute("select test(1, 2)")
my_threading_local.b.execute("select test(1, 2)")
</code>
I'm using Python 3.5.2 and SQLite 3.13.0
