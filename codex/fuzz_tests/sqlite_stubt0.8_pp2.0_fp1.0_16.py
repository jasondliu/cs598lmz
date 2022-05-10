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
    my_threading_local.a.execute('select test(?, ?)', (0, 1))

    return 1

def my_cb3(p):
    del my_threading_local.a
    return 1

def my_cb4(p):
    try:
        my_threading_local.a
    except AttributeError:
        return 1

    return 0

class test_script:
    def __init__(self, uri=False, use_drops=False, use_files=False):
        self.use_files = use_files
        if self.use_files:
            path = tempfile.mktemp()
            self.uri = "file:" + path
        elif uri:
            self.uri = DB_URI
        else:
            self.path = tempfile.mktemp()
            self.uri = None

    def __del__(self):
        if not self.use_files:
            try:
                os.remove(self.path)
            except OSError
