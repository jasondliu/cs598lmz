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
    p = ctypes.CDLL(ctypes.util.find_library('pthread'))
    p.pthread_key_create.restype = ctypes.c_int
    p.pthread_key_create.argtypes = [ctypes.POINTER(ctypes.c_ulong), ctypes.c_void_p]

    p.pthread_setspecific.restype = ctypes.c_int
    p.pthread_setspecific.argtypes = [ctypes.c_ulong, ctypes.c_void_p]

    key_ptr = ctypes.POINTER(ctypes.c_ulong)()
    p.pthread_key_create(key_ptr, my_cb)

    p.pthread_setspecific(key_ptr.contents, ctypes.c_void_p(0x42))

    del p
    del key_ptr

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
   
