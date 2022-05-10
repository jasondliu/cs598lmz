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

def my_fail_cb(p):
    return 1

def init(self, p):
    del p[:]
    p[:] = (13, 42)
    return 1

def ext_from_list(l):
    return l[:]

libc = ctypes.CDLL(ctypes.util.find_library('c'), os.RTLD_GLOBAL)
libctypes = ctypes.CDLL(ctypes.util.find_library('ctypes'), os.RTLD_GLOBAL)

c_flags = None

class H(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
    ]

def test(s='default'):
    libsqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'), os.RTLD_GLOBAL)

    libsqlite.sqlite3_api_routines.restype = ctypes.POINTER(ctypes.c_void_p)

    my_cb_ptr = ctypes.CF
