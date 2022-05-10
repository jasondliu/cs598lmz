import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True, check_same_thread=False)
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True, check_same_thread=False, isolation_level=None)
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True, check_same_thread=False, isolation_level=None, timeout=5.0)
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True, check_same_thread=False, isolation_level=None, timeout=5.0, detect_types=sqlite3.PARSE_DECLTYPES)
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True, check_same_thread=False, isolation_level=None, timeout=
