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

sqlite3.enable_shared_cache(True)


libname = ctypes.util.find_library("m")
clib = ctypes.CDLL(libname, use_errno=True)
clib.malloc.argtypes = [ctypes.c_size_t]
clib.malloc.restype = ctypes.c_void_p

def malloc(size):
    v = clib.malloc(size)
    if v is None:
        errno = ctypes.get_errno()
        if errno:
            raise OSError(errno, os.strerror(errno))
        return None
    return v

clib.free.argtypes = [ctypes.c_void_p]
clib.free.restype = None

def free(ptr):
    clib.free(ptr)

class Thread(threading.Thread):
    def __del__(self):
        try:
            while True:
                fd = self._fdqueue.get_nowait()
                os.
