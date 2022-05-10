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

libc = ctypes.CDLL(ctypes.util.find_library("c"))

libc.pthread_create.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_void_p,
]
libc.pthread_create.restype = ctypes.c_int

posix_fadvise = libc.posix_fadvise
posix_fadvise.restype = ctypes.c_int
posix_fadvise.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

POSIX_FADV_DONTNEED = 4

def unlink():
    posix_fadvise(-1, 0, 0, POSIX_FADV_DONTNEED)
    libc.unlink("test")
