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

def my_cb2(p):
    return 1

def do_stuff():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    a.set_progress_handler(my_cb, 1)

    a.execute("create table test (x int)")
    a.execute("insert into test values (1)")
    a.execute("select test(x) from test")

    a.set_progress_handler(my_cb2, 1)

    a.execute("select x from test")

    a.set_progress_handler(None, None)

    a.execute("select x from test")

if __name__ == "__main__":
    for i in range(10):
        do_stuff()
