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

try:
    ctype_sqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
except:
    print( 'SKIP: sqlite3 shared library not available' )
    sys.exit(0)

ctype_sqlite3.sqlite3_open.restype = ctypes.c_void_p
ctype_sqlite3.sqlite3_close.argtypes = [ctypes.c_void_p]
ctype_sqlite3.sqlite3_close.restype = ctypes.c_int
cb = ctypes.COpaquePointer.in_dll(ctype_sqlite3, 'test_sqlite3_threading_hook')
ctype_sqlite3.sqlite3_thread_cleanup.argtypes = None
ctype_sqlite3.sqlite3_thread_cleanup.restype = None

if ctype_sqlite3.sqlite3_thread_cleanup:
    ctype_sqlite3.sqlite3_thread_cleanup()

