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

lib = sqlite3.load_extension("mod_spatialite.so.7")
print("Loaded something:", lib)

# sqlite3.enable_callback_tracebacks(True)
print("Registering auth")
sqlite3.sqlite3_progress_handler(my_cb, 10000)
print("Starting")
conn = sqlite3.connect(':memory:')

b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
print("Created: ", b)

#lib.dll.spatialite_init_ex(conn._conn_ptr, 1, 1)
# print("installed...")
# ctypes.CDLL("mod_spatialite.so.7").spatialite_init_ex(conn._conn_ptr, 1, 1)

# def f(p):
    # a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    # b = sqlite3.connect(":memory:")
    # print("Created: ",
