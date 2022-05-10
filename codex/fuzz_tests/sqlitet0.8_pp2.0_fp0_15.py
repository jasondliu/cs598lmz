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


def test_starting_threads_and_calling_into_sqlite_at_the_same_time():
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    pthread_create = libc.pthread_create

    # 2nd argument is a pointer to the function
    pthread_create.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

    t = libc.pthread_create(
        ctypes.c_void_p(),
        ctypes.c_void_p(my_cb),
        ctypes.c_void_p()
    )
    if t != 0:
        raise Exception("pthread_create", t)

    def test_thread_fn():
        conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        cur = conn.cursor()
        cur.execute("SELECT test(?, ?)", (3, 5))
        assert cur.fetchone()
