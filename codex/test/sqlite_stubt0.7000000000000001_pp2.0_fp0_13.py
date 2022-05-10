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

def my_cb_final(p):
    del my_threading_local.a
    return 1

def my_test():
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_threading_local.b = b

    for i in range(100):
        my_threading_local.a.execute("select test(?)", (i,))

def test_threading():
    sqlite3.threadsafety.enable_callback_tracebacks(True)
    sqlite3.threadsafety.set_intermediate(my_cb)
    sqlite3.threadsafety.set_intermediate_finalizer(my_cb_final)

    threads = [
        threading.Thread(
            target=my_test
        )
        for i in range(3)
    ]

    for x in threads:
        x.start()

    for x in threads:
        x.join()

print("python", ".".join(map(str, sys.version_info)))
