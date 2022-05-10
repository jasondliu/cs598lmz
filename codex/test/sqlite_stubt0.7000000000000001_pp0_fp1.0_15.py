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

def main(argv):
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_enable_load_extension(None, 1)
    lib.sqlite3_load_extension(None, "./testext.so", None)

    with sqlite3.connect(DB_URI, uri=True, factory=deleting_conn) as conn:
        conn.create_function("my_cb", 0, my_cb)
        cur = conn.cursor()
        cur.execute("SELECT my_cb()")
        cur.execute("SELECT test(1, 2)")
        cur.execute("SELECT test(1, 2)")

    # we're done, on python 3.8+ the value should be GCed now
    # without the patch, the value isn't GCed and the test hangs
    # on python 3.4-3.7, the value is GCed even without the patch

