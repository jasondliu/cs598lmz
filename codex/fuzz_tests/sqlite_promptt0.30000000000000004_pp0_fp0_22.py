import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
# Test sqlite3.connect('file:memory:?cache=shared', uri=True, check_same_thread=False)
# Test sqlite3.connect('file:memory:?cache=shared', uri=True, check_same_thread=False, isolation_level=None)
# Test sqlite3.connect('file:memory:?cache=shared', uri=True, check_same_thread=False, isolation_level=None, detect_types=0)
# Test sqlite3.connect('file:memory:?cache=shared', uri=True, check_same_thread=False, isolation_level=None, detect_types=0, factory=None)
# Test sqlite3.connect('file:memory:?cache=shared', uri=True, check_same_thread=False, isolation_level=None, detect_types=0, factory=None, timeout=5.0)
# Test sqlite3.connect('file:memory:?cache=shared', uri=True, check_same_thread=
