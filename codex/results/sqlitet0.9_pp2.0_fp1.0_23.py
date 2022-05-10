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

pthread = ctypes.CDLL(ctypes.util.find_library("pthread"))
cb_func = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
pthread.pthread_create.argtypes = [
                                 ctypes.POINTER(ctypes.c_void_p),
                                 ctypes.c_void_p,
                                 ctypes.c_void_p,
                                 ctypes.c_void_p
                                 ]
ptr = ctypes.c_void_p()
ptr_ptr = ctypes.pointer(ptr)
pthread.pthread_create(ptr_ptr, None, cb_func, None)
pthread.pthread_join(ptr, None)

print(my_threading_local.a)
my_threading_local.a.close()
try:
    my_threading_local.a.execute("select * from test")
except RuntimeError as e:
    print("ACTUAL ERROR: {}".format(e))


