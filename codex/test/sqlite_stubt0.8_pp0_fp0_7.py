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


def test_init():
    try:
        sqlite3.sqlite_version_info
    except:
        raise ImportError("Your pysqlite does not include the sqlite3.sqlite_version_info constant. You probably have an old, deprecated version of pysqlite installed (pysqlite2).\nPlease install the pysqlite3 package via 'pip install pysqlite3' and try again.")
    if not os.environ.get('SQLITE_DBCORE_ENABLED', '').lower() in ('1', 'true'):
        raise ImportError("Environment variable SQLITE_DBCORE_ENABLED not set or not set to True.\n"
                          "Please set it to True to use the `dbcore` module (and be aware that the `sqlite3` "
                          "module is not a supported public API).\n"
                          "Note that this check only applies when using the C extension, not the pure Python "
                          "implementation.")
