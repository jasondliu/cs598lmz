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

ll = ctypes.CDLL(ctypes.util.find_library('c'))
ll.pthread_create.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
ll.pthread_join.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

my_cb_c = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)

thread = ctypes.c_void_p()
ll.pthread_create(ctypes.byref(thread), None, my_cb_c, None)
ll.pthread_join(thread, None)

a = my_threading_local.a

a.set_trace_callback(print)

a.execute('select test(1, 2);')
