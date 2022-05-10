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

sqlite3.set_authorizer(my_cb)

libc = ctypes.CDLL(ctypes.util.find_library("c"))

def my_add_cb(a, b, c, d):
    libc.malloc(1)

    return 0

libc.pthread_key_create.argtypes = [ctypes.POINTER(ctypes.c_long), ctypes.c_void_p]
key = ctypes.c_long()
libc.pthread_key_create(ctypes.byref(key), my_add_cb)

def my_del_cb(a, b):
    libc.free(a)

libc.pthread_setspecific.argtypes = [ctypes.c_long, ctypes.c_void_p]
libc.pthread_setspecific(key, libc.malloc(1))

p1 = threading.Thread(target=sqlite3.connect,
                args=(DB_URI,),
                kwargs={"uri":True, "
