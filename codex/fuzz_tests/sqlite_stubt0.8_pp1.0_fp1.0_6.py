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

my_cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
my_cb_ptr = my_cb_type(my_cb)

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
lib.sqlite3_auto_extension(my_cb_ptr)

conn = sqlite3.connect(DB_URI, uri=True)
curs = conn.cursor()

curs.execute("SELECT test('1234', ?)", (5,))
assert curs.fetchone() == ('1234',)

del my_threading_local.a
