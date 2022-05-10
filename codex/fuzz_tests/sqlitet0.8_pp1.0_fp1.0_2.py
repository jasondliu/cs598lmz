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

if __name__ == '__main__':
    try:
        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

        name = ctypes.util.find_library('sqlite3')
        if not name:
            raise RuntimeError("Unable to find sqlite library")

        sqlite3.sqlite_version_info
        sqlite3.sqlite_version

        lib = ctypes.CDLL(name)
        cf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))
        p = ctypes.c_int(0)

        cb = cf(my_cb)
        lib.sqlite3_shutdown()
        lib.sqlite3_config(ctypes.c_int(0x00060000), cb, ctypes.byref(p))
        lib.sqlite3_initialize()

        a.execute("create table foo(x)")
        a.execute("insert into foo(x) values (1
