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

class SQLiteThreading(unittest.TestCase):
    def setUp(self):
        self.thread_count = 20
        self.threads = []
        self.p = ctypes.c_void_p()
        self.error = sqlite3.sqlite3_open(DB_URI, ctypes.byref(self.p))

    def tearDown(self):
        sqlite3.sqlite3_close(self.p)

    def spawn_thread(self):
        t = threading.Thread(target=self.thread_fn)
        self.threads.append(t)
        t.start()

    def thread_fn(self):
        sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(self.p),
            sqlite3.SQLITE_OPEN_READWRITE, None)
        sqlite3.sqlite3_exec(self.p, "BEGIN", None, None, None)
        sqlite3.sqlite3_create_function(self.p, "test",
