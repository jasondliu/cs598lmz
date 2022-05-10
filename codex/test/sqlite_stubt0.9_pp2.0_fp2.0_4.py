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

_init_sqlite3_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

def load_static_sqlite(sqlite_libname=None):
    if sqlite_libname is None:
        sqlite_libname = ctypes.util.find_library('sqlite3')

    if sqlite_libname is None:
        raise RuntimeError(
                "Could not load static sqlite3 library, " \
                "tried directories: %s, sqlite_libname: %s" % (
                        os.environ['PATH'].split(os.pathsep), \
                        sqlite_libname))

    if os.name=='nt':
        # XXX: on Windows, turn off generics - does anyone know why?
        ctypes.cdll.LoadLibrary(sqlite_libname)
    sqlite3 = ctypes.CDLL(sqlite_libname, use_errno=True)

    return sqlite3

sqlite3 = load_static_
