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

sqlite3.register_progress_handler(my_cb, 1)

try:
    ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_enable_shared_cache(1)
except:
    pass

def iter_fun():
    for i in xrange(100):
        a = sqlite3.connect(DB_URI, uri=True)
        a.cursor().execute("SELECT * FROM test;")
        yield i

for i in iter_fun():
    pass
