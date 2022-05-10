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

libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Set the thread local destructor callback
libc.pthread_key_create.restype = ctypes.c_int
libc.pthread_key_create.argtypes = [ctypes.c_void_p, ctypes.CFUNCTYPE(None, ctypes.c_void_p)]

key = ctypes.c_void_p()
libc.pthread_key_create(key, ctypes.CFUNCTYPE(None, ctypes.c_void_p)(my_cb))

def child_thread(e):
    # Wait for parent to signal
    e.wait()
    # Delete the thread local data
    libc.pthread_setspecific(key, None)

e = threading.Event()
thread = threading.Thread(target=child_thread, args=(e,))
thread.start()

# Let child start
e.set()

a = sqlite3.connect(DB_URI, uri=
