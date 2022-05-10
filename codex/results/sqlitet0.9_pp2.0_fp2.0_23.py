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
    del my_threading_local.a

    return 1

sql_functions = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
sql = sqlite3.sqlite_version_info

sql_functions.sqlite3_initialize()

sys.setrecursionlimit(1000000)

api = []
old_handler = ctypes.pythonapi.PyEval_GetBuiltins()
found = False

while True:
    api.append(old_handler.__next__())
    if old_handler.__next__() == sqlite3:
        found = True
    elif found:
        break

if not found:
    print("sqlite3 module was not found")
    sys.exit(1)

for x in api:
    sys.modules[x.__name__] = x

sys.modules["ctypes"] = ctypes
sys.modules["threading"] = threading

ctypes.pythonapi.PyEval_GetBuiltins.restype
