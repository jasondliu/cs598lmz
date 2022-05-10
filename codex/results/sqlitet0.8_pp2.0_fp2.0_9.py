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
    my_threading_local.a = None
    return 0

def cb_wrapper():
    return ctypes.pythonapi.Py_MakePendingCalls(my_cb, my_cb2)

def test_callback():
    my_threading_local.a = None

    assert not my_threading_local.a

    ctypes.pythonapi.Py_MakePendingCalls(my_cb, my_cb2)

    assert my_threading_local.a

    with sqlite3.connect(DB_URI, uri=True, factory=deleting_conn) as conn:
        cursor = conn.cursor()
        assert my_threading_local.a == conn
        cursor.execute("select test(?, ?)", (0, 0))
    assert not my_threading_local.a

def test_callback_thread():
    my_threading_local.a = None

    assert not my_threading_local.a

    t = threading.Thread(target=cb_wrapper)
