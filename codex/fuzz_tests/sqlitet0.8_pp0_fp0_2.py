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

def test_no_memory_leaks_from_sqlite3_connect(self):
    # o == connection
    o = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
</code>
And I run it with:
<code>./python.exe ./python.exe -m unittest test
</code>
It doesn't pick up the functions.
How do I use this to test the functions?
How do I test the thread_local variable?

