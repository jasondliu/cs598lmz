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

    return 100

def my_initialize(x):
    pass

def my_shutdown(x):
    pass

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_enable_load_extension(1)
lib.sqlite3_config(0x02, 0)
lib.sqlite3_auto_extension(ctypes.pythonapi.PyCObject_AsVoidPtr(my_cb))
lib.sqlite3_config(0x1b, ctypes.pythonapi.PyCObject_AsVoidPtr(my_initialize))
lib.sqlite3_config(0x1c, ctypes.pythonapi.PyCObject_AsVoidPtr(my_shutdown))

connection = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
cursor = connection.cursor()
cursor.execute("create table test (id integer)")
connection.commit()

connection2 = sqlite3.connect(DB_URI, uri=True, factory
