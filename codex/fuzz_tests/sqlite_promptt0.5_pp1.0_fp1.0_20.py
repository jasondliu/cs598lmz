import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
# Test sqlite3.connect('file:memory:?cache=private', uri=True)
# Test sqlite3.connect('file:memory:?cache=shared', uri=True, check_same_thread=False)
# Test sqlite3.connect('file:memory:?cache=private', uri=True, check_same_thread=False)

# Test sqlite3.connect(':memory:', uri=True)
# Test sqlite3.connect(':memory:', uri=True, check_same_thread=False)

# Test sqlite3.connect('file::memory:?cache=shared', uri=True)
# Test sqlite3.connect('file::memory:?cache=shared', uri=True, check_same_thread=False)

# Test sqlite3.connect('file::memory:?cache=shared', uri=False)
# Test sqlite3.connect('file::memory:?cache=shared', uri=False, check_same_thread=False)
