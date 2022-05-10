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

    return 10

my_cb_addr = id(my_cb)
my_cb_ptr = ctypes.cast(my_cb_addr, ctypes.POINTER(ctypes.c_void_p))

lib_handle = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

# setup the sqlite3_vfs
vfs_rc = lib_handle.sqlite3_vfs_register(
    lib_handle.sqlite3_vfs_find("unix"), True)

# setup the sqlite3_vfs
vfs_ptr = lib_handle.sqlite3_vfs_find("unix")

# setup the sqlite3_vfs_sensitive
vfs_sens_create = ctypes.cast(lib_handle.sqlite3_vfs_sensitive_create, ctypes.CFUNCTYPE(
                    ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)))
vfs_ptr.pAppData
