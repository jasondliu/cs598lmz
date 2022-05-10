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


# Obtain the function pointer to sqlite3_create_function_v2
if sys.platform == 'darwin':
    fname = ctypes.util.find_library('libsqlite3')
else:
    fname = ctypes.util.find_library('sqlite3')
if not fname:
    raise RuntimeError('sqlite3 library not found')
sqlite3lib = ctypes.CDLL(fname)

sqlite3_create_function_v2 = sqlite3lib.sqlite3_create_function_v2
sqlite3_create_function_v2.restype =  ctypes.c_int
sqlite3_create_function_v2.argtypes = (
    ctypes.c_void_p, # sqlite3 *db
    ctypes.c_char_p, # const char *zFunctionName
    ctypes.c_int, # int nArg
    ctypes.c_int, # int eTextRep
    ctypes.c_void_p, # void *pApp
    ctypes.POINTER(
