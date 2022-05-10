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

def my_cb2(p):
    try:
        my_threading_local.a.execute("select test(1, 2)")
    except:
        print("Error:", sys.exc_info())
        sys.exit(1)

    return 1

if __name__ == '__main__':
    libpthread = ctypes.CDLL(ctypes.util.find_library("pthread"))
    libsqlite3 = ctypes.CDLL("libsqlite3.so.0")

    # register callback
    libsqlite3.sqlite3_initialize()
    old_cb = libsqlite3.sqlite3_thread_cleanup
    libsqlite3.sqlite3_thread_cleanup = my_cb

    # create thread
    pthread = libpthread.pthread_create(threading.Thread, None, my_cb2, None)
    libpthread.pthread_join(pthread, None)

    # unregister callback
    libsqlite3.sqlite3_thread_cleanup = old_cb
