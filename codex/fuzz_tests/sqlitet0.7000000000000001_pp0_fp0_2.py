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

def my_cb_wrapper():
    return sqlite3.sqlite3_progress_handler(my_cb, 0, 0)

ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_progress_handler.argtypes = [sqlite3.sqlite3_callback, sqlite3.c_int, sqlite3.c_int]
ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_progress_handler(my_cb_wrapper, 1, 1)

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

c = conn.cursor()
c.execute("select test(1, 2)")

c = my_threading_local.a.cursor()
c.execute("select test(1, 2)")
</code>
If you run this code with Python 3.5 or later, it will print out:
<code>Selecting function test
Selecting function test
</code>
If you run this code
