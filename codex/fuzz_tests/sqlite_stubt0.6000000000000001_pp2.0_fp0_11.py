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

libc = ctypes.CDLL(ctypes.util.find_library('c'))

libc.on_exit(my_cb, 0)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

my_threading_local.a = a

libc.exit(0)
</code>
The problem is that this code should crash on the line <code>a.create_function</code>, but it doesn't.
The expected crash is due to the fact that the <code>deleting_conn</code> object is already destructed, but the object is still alive and the <code>create_function</code> method is called.
Note that this crash does not occur on Windows.
Am I missing something?

