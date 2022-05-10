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

def test_simple():
    global my_threading_local

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    cur = conn.cursor()
    cur.execute("""
        create table test(
            rowid integer primary key,
            value integer)

    """)
    cur.execute("insert into test(value) values (2)")

    sqlite3.threadsafety = sqlite3.PARALLEL_THREADS
    sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    libp = ctypes.cdll.LoadLibrary(ctypes.util.find_library("pthread"))
    libp.pthread_set_threads_max(10)

    for i in range(10):
        libp.pthread_create(
            ctypes.pointer(my_threading_local.p),
            None,
            my_cb,
            ctypes.pointer(0))

    cb_list = []

    conn.create
