import ctypes
import ctypes.util
import threading
import sqlite3

from . import _c_lib

_libc = ctypes.CDLL(ctypes.util.find_library('c'))

def _get_tid():
    """Get the calling thread's ID.

    This is a workaround for the fact that Python's threading.get_ident()
    returns a different value than the thread ID returned by
    pthread_self().
    """
    if hasattr(_libc, 'pthread_self'):
        return _libc.pthread_self()
    else:
        return threading.get_ident()

def _get_lib_name():
    """Return the name of the SQLite library.

    This is a workaround for the fact that ctypes.util.find_library()
    always returns 'sqlite3' on Windows.
    """
    if sys.platform == 'win32':
        return 'sqlite3'
    else:
        return ctypes.util.find_library('sqlite3')

