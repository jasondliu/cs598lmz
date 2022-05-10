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

def my_cb_3(p):
    try:
        return my_threading_local.a.test(1, 2)
    except sqlite3.ProgrammingError:
        return None

def my_cb_4(p):
    try:
        my_threading_local.a.non_existent_function(1)
    except sqlite3.ProgrammingError:
        return 1

def my_cb_5(p):
    try:
        my_threading_local.a.execute("select nonexistent_function(1)")
    except sqlite3.OperationalError:
        return 1

def my_cb_6(p):
    try:
        my_threading_local.a.execute("select test(1, 2)")
    except sqlite3.OperationalError:
        return 1

def my_cb_7(p):
    try:
        my_threading_local.a.execute("
