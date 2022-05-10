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
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    try:
        b.execute("SELECT test(42, ?)", (my_threading_local.a,))
    except sqlite3.ProgrammingError:
        b.close()
        return 0

    b.close()
    return 1

def my_cb3(p):
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    try:
        b.execute("SELECT ?", (my_threading_local.a,))
    except sqlite3.ProgrammingError:
        b.close()
        return 0

    b.close()
    return 1

def my_cb4(p):
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    try:
        b.execute("SELECT ?", (p,))
    except sqlite3.ProgrammingError:
       
