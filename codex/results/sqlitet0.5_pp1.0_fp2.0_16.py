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
    my_threading_local.a.close()

    return 1

def get_sqlite3_lib():
    if sys.platform == "darwin":
        lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    else:
        lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3.so.0"))

    return lib

def test_sqlite3_threading_issue():
    lib = get_sqlite3_lib()

    lib.sqlite3_config(1, my_cb, my_cb2)

    conn = sqlite3.connect(DB_URI, uri=True)
    cursor = conn.cursor()

    cursor.execute("select test(?, ?)", (1, 2))
    cursor.fetchall()

    cursor.close()
    conn.close()

    lib.sqlite3_config(1, None, None)

def test_sqlite3_threading_issue_
