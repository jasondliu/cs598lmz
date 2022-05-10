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

clibrary = ctypes.CDLL(ctypes.util.find_library('c'))
try:
    from ctypes import wintypes
except ImportError:
    if sys.platform == 'win32':
        raise
    class wintypes(object):
        DWORD = None

STD_OUTPUT_HANDLE = -11

if sys.platform == 'win32' and wintypes:
    class _COORD(ctypes.Structure):
        _fields_ = [('X', wintypes.SHORT),
                    ('Y', wintypes.SHORT)]

    class _SMALL_RECT(ctypes.Structure):
        _fields_ = [('Left', wintypes.SHORT),
                    ('Top', wintypes.SHORT),
                    ('Right', wintypes.SHORT),
                    ('Bottom', wintypes.SHORT)]

    class _CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
        _fields_ = [('dwSize', _COORD),
                    ('dwCursor
