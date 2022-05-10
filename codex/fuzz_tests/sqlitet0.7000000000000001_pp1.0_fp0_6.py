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

sqlite3.enable_shared_cache(True)

# get addresses for the SQLite shared library and the Python function callback
db_path = ctypes.util.find_library('sqlite3')
dll = ctypes.CDLL(db_path)
fn_addr = ctypes.addressof(my_cb)

# call the sqlite3_open_v2 function
dll.sqlite3_open_v2(
    bytes("test", "utf8"),  # database name
    ctypes.pointer(ctypes.c_void_p()),  # database handle
    0x000008,  # SQLITE_OPEN_URI | SQLITE_OPEN_SHAREDCACHE
    bytes("", "utf8"),  # VFS
    fn_addr  # sqlite3_open_v2 callback
)

# spawn threads that do some database activity
for i in range(10):
    t = threading.Thread(target=lambda: my_threading_local.a.execute("select test(?, ?)", (1, 2)).fetchall())
