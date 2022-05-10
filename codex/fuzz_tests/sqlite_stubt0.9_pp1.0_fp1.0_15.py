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

def my_cb_add(p):
    my_threading_local.a.cursor().execute("INSERT INTO test (i) VALUES (1)")
    return 0

def my_cb_del(p):
    try:
        del my_threading_local.a
        return 0
    except AttributeError:
        # If the connection was already deleted, ignore the error;
        # we're not interested in whether it's already been deleted but
        # more of a random check that deleting the connection doesn't
        # affect the thread-local
        return 0

# create our library instance
lib = ctypes.pydll.LoadLibrary(ctypes.util.find_library("sqlite3"))

# be explicit to make sure malloc and friends don't get used
# by byte string functions
lib.create_test_db.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
lib.create_test_db.restype = ctypes.c_int

lib.create_test_db(
