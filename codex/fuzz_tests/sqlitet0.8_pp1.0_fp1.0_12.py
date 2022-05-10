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


class SQLite3Test(unittest.TestCase):
    def test_callback(self):
        sqlite3.enable_callback_tracebacks(True)

        self.p = p = ctypes.util.find_library('sqlite3')
        if not p:
            self.skipTest("unable to find sqlite3 library")

        sqlite3.sqlite_version = "3.7.0"

        from cffi import FFI
        ffi = FFI()
        ffi.cdef("""
        extern esize_t strlen(const char *s);
        typedef unsigned long esize_t;
        int (*sqlite3_open)(const char *filename, void **ppDb);
        int (*sqlite3_close)(void *pDb);
        int (*sqlite3_exec)(void *pDb, const char *sql, void *callback, void *test, char **errmsg);
        int (*sqlite3_config)(int mode, ...);
        int (*sqlite3_create_function)(void *pDb, const char
