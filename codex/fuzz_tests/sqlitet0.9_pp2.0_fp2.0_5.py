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

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))

lib.sqlite3_free_table.restype = None
lib.sqlite3_get_table.argtypes = [
    ctypes.c_void_p, #sqlite3*
    ctypes.c_char_p, #nchar*
    ctypes.POINTER(ctypes.c_char_p), #char**
    ctypes.POINTER(ctypes.c_int), #int*
    ctypes.POINTER(ctypes.c_int), #int*
    ctypes.POINTER(ctypes.c_void_p), #char**
]
lib.sqlite3_get_table.restype = ctypes.c_int

conn = sqlite3.connect(DB_URI, uri=True)
conn.set_progress_handler(my_cb, 100)

lib.sqlite3_get_table(
    conn,
    b"select test('foo', 'bar')",
    None,
   
