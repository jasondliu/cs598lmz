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

def main():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    conn.create_collation('locale_upper', collation)

    assert conn.execute("select \"foo\" = \"Foo\"").fetchall()[0][0] == 1
    conn.create_collation('locale_lower', locale_lower)
    assert conn.execute("select \"foo\" = \"Foo\"").fetchall()[0][0] == 1
    # Make sure our collation is called for case-insensitive comparisons
    assert conn.execute("SELECT sqlite_user_collate('locale_lower')").fetchall()[0][0] == 'locale_lower'
    sqlite3.load_extension(ctypes.util.find_library('sqlite3'), "sqlite3_db_init")

    conn.create_function("test", 1, test_fn)

    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sql
