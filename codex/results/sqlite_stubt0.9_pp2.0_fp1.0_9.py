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

sqlite3.register_python_builtin(my_cb)

def test_my_cb():
    i = 0
    while True:
        sqlite3.enable_callback_tracebacks(True)
        c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        c = None

        i += 1
        if i % 1000 == 0:
            print i

        if ctypes.sizeof(ctypes.pythonapi.PyThreadState_GetDict()) < ctypes.sizeof(ctypes.c_void_p):
            # python 2.6
            gc.collect()


def profile_threaded():
    t1 = threading.Thread(target=profile_threaded_target, args=())
    t2 = threading.Thread(target=profile_threaded_target, args=())
    t3 = threading.Thread(target=profile_threaded_target, args=())
    t1.start()
    t2.start()
    t3.start()
    t1.join
