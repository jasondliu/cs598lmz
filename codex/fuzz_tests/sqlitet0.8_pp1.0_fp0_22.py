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
    a = my_threading_local.a
    a.execute("CREATE TABLE t (id INTEGER PRIMARY KEY AUTOINCREMENT, x INTEGER);")
    for i in range(10):
        a.execute("INSERT INTO t (x) VALUES (?)", (i,))
    return 2

def my_cb3(p):
    a = my_threading_local.a
    cur = a.cursor()
    cur.execute("SELECT test(x, x) from t")
    for row in cur:
        print(row)
    return 3

def my_cb4(p):
    a = my_threading_local.a
    a.close()
    return 4

def main():
    global sqlite3
    sqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    sqlite3.sqlite3_open.restype = ctypes.c_int
    sqlite3.sqlite3_open.argtypes
