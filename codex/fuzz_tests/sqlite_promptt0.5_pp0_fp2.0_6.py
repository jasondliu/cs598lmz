import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:').execute('select sqlite_version()').fetchall()

# See http://www.sqlite.org/c3ref/c_blob.html
SQLITE_BLOB = 4


def _load_libsqlite3():
    """Load and return the sqlite3 library.

    First try to load the system sqlite3 library. If that fails, try
    to load the bundled sqlite3 library.
    """
    try:
        return ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    except:
        if sys.platform == 'win32':
            libname = 'sqlite3.dll'
        elif sys.platform == 'darwin':
            libname = 'libsqlite3.dylib'
        else:
            libname = 'libsqlite3.so'
        return ctypes.CDLL(os.path.join(os.path.dirname(__file__), libname))

_libsqlite3 = _load_libsqlite3()


def _sqlite3_check_
