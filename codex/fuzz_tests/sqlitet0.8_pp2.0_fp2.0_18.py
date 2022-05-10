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

def my_cb_dbl(p):
    my_threading_local.a.close()
    my_threading_local.a = None

    return 1

def test_callback_thread_safe():
    p = ctypes.Pointer(ctypes.c_int())

    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    if hasattr(libc, "pthread_create"):
        pthread_create = libc.pthread_create

        class _thread(threading.Thread):
            def __init__(self, p):
                threading.Thread.__init__(self)
                self.p = p

            def run(self):
                self.p.contents.value = my_cb(self.p)

        thread_0 = _thread(p)
        thread_1 = _thread(p)

        thread_0.start()
        thread_1.start()

        thread_0.join()
        thread_1.join()

        assert my_threading_local.a is
