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

def test_fn(a, b):
    return a

def test_sqlite_threading():
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.create_function("test", 2, test_fn)

    t = threading.Thread(target=my_cb, args=(conn,))
    t.start()
    i = 0
    while t.is_alive():
        try:
            my_threading_local.a.execute("select test(1, 2)").fetchall()
            i += 1
        except:
            pass
    assert i > 0

def test_sqlite_threading_serialized():
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.create_function("test", 2, test_fn)

    t = threading.Thread(target=my_cb, args=(conn,))
    t.start()
    i = 0
