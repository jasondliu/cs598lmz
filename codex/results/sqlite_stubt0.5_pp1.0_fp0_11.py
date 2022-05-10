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

def my_cb_2(p):
    my_threading_local.a.close()
    return 1

if __name__ == '__main__':
    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    c.create_function("test", 1, my_cb)
    c.create_function("test2", 1, my_cb_2)
    c.execute("select test(?)", (1,))
    c.execute("select test2(?)", (1,))
    c.execute("select test(?)", (1,))
    c.execute("select test2(?)", (1,))
