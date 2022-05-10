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

def my_thread():
    time.sleep(1)

    a = my_threading_local.a
    a.execute("SELECT test (1, 1)")

    try:
        a.execute("SELECT test (1, 1)")
    except sqlite3.ProgrammingError as e:
        assert "not an error" not in str(e)
        return 1

    assert "not an error"

    return 0

sqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True)
sqlite3.sqlite3_interrupt.argtypes = []
sqlite3.sqlite3_interrupt.restype = None

load = ctypes.cdll.LoadLibrary("./dbload.so")
load.load(128, my_cb)

t = threading.Thread(target=my_thread, args=[])
t.start()

for i in range(0, 100):
    try:
        sqlite3.sqlite3_interrupt()
    except:
        pass
