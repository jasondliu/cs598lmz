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

ctypes.pythonapi.Py_AddPendingCall(ctypes.c_int, ctypes.py_object)
ctypes.pythonapi.Py_AddPendingCall.argtypes = [ctypes.c_int, ctypes.py_object]
ctypes.pythonapi.Py_AddPendingCall.restype = ctypes.c_int
ctypes.pythonapi.Py_AddPendingCall(my_cb, None)

def test_fn(a, b):
    return a

conn = sqlite3.connect(DB_URI, uri=True)
conn.create_function("test", 2, test_fn)
cur = conn.cursor()
cur.execute("SELECT test(1, 2)")
print(cur.fetchone())

print('-'*20)

conn = my_threading_local.a
cur = conn.cursor()
cur.execute("SELECT test(1, 2)")
print(cur.fetchone())
</code>

