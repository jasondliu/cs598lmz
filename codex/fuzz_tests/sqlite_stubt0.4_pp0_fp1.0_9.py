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
    lib = ctypes.util.find_library("sqlite3")
    if lib is None:
        lib = "libsqlite3.so"
    sqlite3.sqlite_version_info = tuple(map(int, sqlite3.sqlite_version.split(".")))
    sqlite3.sqlite_version_number = sqlite3.sqlite_version_info[0] * 1000000 + sqlite3.sqlite_version_info[1] * 1000 + sqlite3.sqlite_version_info[2]
    sqlite3.sqlite_version = ".".join(map(str, sqlite3.sqlite_version_info))
    sqlite3.sqlite_version_info = tuple(map(int, sqlite3.sqlite_version.split(".")))
    sqlite3.sqlite_version_number = sqlite3.sqlite_version_info[0] * 1000000 + sqlite3.sqlite_version_info[1] * 1000 + sqlite3.sqlite_version_info[2]

