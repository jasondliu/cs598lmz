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

    return 100

def main():
    """
    The following errors indicated that there is a bug:
    """
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    conn.execute("CREATE TABLE users (firstname, lastname);")
    conn.execute("INSERT INTO users VALUES ('john', 'doe');")
    conn.execute("INSERT INTO users VALUES ('mark', 'smith');")

    res = conn.execute("SELECT test(firstname, :dom) FROM users;", {"dom": "e"})

    assert(res.fetchall() == [(u'john',), (u'mark',)])

    del conn

    dll_path = ctypes.util.find_library("libpython2.7")
    if dll_path is None:
        raise Exception("Can't find libpython2.7 dll")

    gc_dll = ctypes.CDLL(dll_path, use_errno=True)

    gc.enable()
    print gc_dll.PyGC_Collect()
