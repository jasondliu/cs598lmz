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

def my_cb_stub(p):
    return 1

def my_cb_stub_del(p):
    del my_threading_local.a
    return 1

GET_RTLD_GLOBAL = 0x100
RTLD_LAZY = 1
RTLD_GLOBAL = 2
RTLD_LOCAL = 4

libsqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
assert hasattr(libsqlite3, 'sqlite3_config')
assert hasattr(libsqlite3, 'sqlite3_initialize')
assert hasattr(libsqlite3, 'sqlite3_open')
assert hasattr(libsqlite3, 'sqlite3_enable_load_extension')

libdl = ctypes.cdll.LoadLibrary(ctypes.util.find_library('dl'))

# Load a newer version of sqlite3 than the system-provided one
