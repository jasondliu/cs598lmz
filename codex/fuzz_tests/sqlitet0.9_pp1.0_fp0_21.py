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

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
print(a)
clib = ctypes.CDLL(ctypes.util.find_library('c'))
a.create_function('bar', 1, test_fn)
a.create_function('foo', 0, my_cb)
a.execute('select foo()')
print(my_threading_local.a)
del my_threading_local
print(a)
clib.exit(0)
