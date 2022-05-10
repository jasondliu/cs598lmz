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

def my_thread_init(x):
    return 0

def my_func(a):
    b = my_threading_local.a.execute("select test(1, 2)").fetchone()[0]

    return 1

def my_threadfunc():
    libsqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    x = ctypes.byref(ctypes.c_void_p(libsqlite))
    libsqlite.sqlite3_config(ctypes.c_int(45), ctypes.c_int(my_cb), x);
    return

my_thread = threading.Thread(target=my_threadfunc, args=())
my_thread.setDaemon(True)
my_thread.start()

libsqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
libsqlite.sqlite3_initialize()
libsqlite.sqlite3_shutdown()

libsqlite = ctypes.CDLL(ctypes.util
