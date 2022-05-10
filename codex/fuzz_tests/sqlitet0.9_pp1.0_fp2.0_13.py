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

if not hasattr(pthread, 'pthread_setspecific'):
    print("[SKIP] This platform doesn't have pthread_setspecific.")
    sys.exit(0)

pthread.pthread_setspecific.restype = ctypes.c_int
pthread.pthread_setspecific.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

a = sqlite3.connect(DB_URI, uri=True)

pthread.pthread_key_create.argtypes = [ctypes.c_void_p]
pthread.pthread_key_create(ctypes.byref(ctypes.c_void_p(ctypes.addressof(my_threading_local))))
pthread.pthread_key_create(ctypes.byref(ctypes.c_void_p(ctypes.addressof(a))))

a.create_function("callback", 1,
