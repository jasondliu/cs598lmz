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


class MyThread(threading.Thread):
    def run(self):
        b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        my_threading_local.b = b

        b.set_authorizer(my_cb)

        b.execute("select test(1,2)")
        b.execute("select test(1,2)")
        b.execute("select test(1,2)")
        b.execute("select test(1,2)")
        b.execute("select test(1,2)")
        b.execute("select test(1,2)")

        c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        my_threading_local.c = c
        c.execute("select test(1,2)")
        c.execute("select test(1,2)")
        c.execute("select test(1,2)")
        c.execute("select test(1,2)")
        c.execute("
