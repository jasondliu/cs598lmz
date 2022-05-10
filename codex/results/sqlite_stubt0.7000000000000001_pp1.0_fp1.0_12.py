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

p = ctypes.pointer(ctypes.c_int(0))

print(ctypes.util.find_library("sqlite3"))

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))

def test_fn(a, b):
    return a

sqlite3.enable_callback_tracebacks(True)

sqlite3.register_adapter(str, lambda s: s.encode())

sqlite3.connect(DB_URI, uri=True, factory=deleting_conn, check_same_thread=False).close()

time.sleep(10)

ctypes.pythonapi.Py_AddPendingCall(ctypes.pythonapi.PyThreadState_Get(), my_cb, p)

time.sleep(10)

print(lib.sqlite3_threadsafe())

lib.sqlite3_shutdown()
