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

try:
    if CURRENT_DBAPI_VERSION_STRING[:3] == "3.12":
        lib = ctypes.cdll.LoadLibrary("libsystem.dylib")
        lib.sem_unlink.restype = ctypes.c_int
        lib.sem_unlink.argtypes = [ctypes.c_int]
        lib.sem_unlink("/sem.test")
except AttributeError:
    pass

sqlite3.enable_callback_tracebacks(True)
con = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
con.set_progress_handler(my_cb, 100)
cur = con.cursor()
try:
    with pytest.raises(sqlite3.OperationalError):
        cur.execute("CREATE TABLE t(i)")
finally:
    del cur
    del con

sys.stderr.truncate(0)
cur = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn
