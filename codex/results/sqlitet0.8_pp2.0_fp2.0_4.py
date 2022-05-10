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

lib = ctypes.CDLL(ctypes.util.find_library("System"), use_errno=True)
lib.system.argtypes = (ctypes.c_char_p,)
lib.system.restype = ctypes.c_int

lib.set_threadpool_callbacks(my_cb, None, None, None)
lib.initialize_thread_pool(None, None)

threads = []
for i in range(2):
    thread = threading.Thread(target=lib.system, args=(b"ls",))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

lib.shutdown_thread_pool()
