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

# We use pthreads to create an context where the thread state will get
# torn down after invocation

libpthread = ctypes.CDLL(ctypes.util.find_library('pthread'))

cb = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

pthread_t = ctypes.c_ulong

pthread_create_proto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(pthread_t), ctypes.c_void_p, cb, ctypes.c_void_p)
pthread_create = pthread_create_proto(("pthread_create", libpthread))

pthread_join_proto = ctypes.CFUNCTYPE(ctypes.c_int, pthread_t, ctypes.POINTER(ctypes.c_void_p))
pthread_join = pthread_join_proto(("pthread_join", libpthread))

thread_id = pthread_t()

wrapped_cb = cb(my_cb)

thread_arg = ctypes.c_void_p(2)

ret = pthread_create(ctypes.byref(thread_id), None, wrapped_cb, thread_arg)
if ret:
    raise Exception("error calling pthread_create: %d" % (ret,))

retval = ctypes.c_void_p()
ret = pthread_join(thread_id, ctypes.byref(retval))
if ret:
    raise Exception("error calling pthread_join: %d" % (ret,))
