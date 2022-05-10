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

class MyError(Exception):
    def __init__(self, errno):
        self.args = (errno,)

sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

p = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_test_control
p.argtypes = [ctypes.c_int, ctypes.c_void_p]

p(1, my_cb)
del p
my_threading_local.a.execute("SELECT test(?);", (MyError(42),))
</code>
The crash was reproducible with python 2.7 and 3.5, both with pysqlite 2.6.3 and 2.8.2.
Also, I left out the <code>sqlite3_threadsafe()</code> check in the example, but otherwise it should be equivalent to the real life code. It's a Tornado app (i.e. one process, multiple threads).


A:

In sqlite3.py, when you do

