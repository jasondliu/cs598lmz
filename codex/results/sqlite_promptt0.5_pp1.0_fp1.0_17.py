import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:').execute('select 1').fetchall()

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from . import util

try:
    from . import _lib
except ImportError:
    _lib = None

try:
    from . import _lib_dummy
except ImportError:
    _lib_dummy = None

_lib_dummy_mutex = threading.Lock()

_lib_dummy_mutex.acquire()

_lib_dummy_db = _lib_dummy.sqlite3_open(':memory:')

_lib_dummy_mutex.release()

_lib_dummy_stmt_mutex = threading.Lock()

_lib_dummy_stmt_mutex.acquire()

_lib_dummy_stmt = _lib_dummy.sqlite3_prepare_v2(_lib_dummy_db, 'select 1', -1)

_lib_dummy_stmt_mutex
