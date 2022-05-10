import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
# Test sqlite3.connect('file:memory:?cache=private')
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
# Test sqlite3.connect('file:memory:?cache=private', uri=True)
# Test sqlite3.connect(':memory:?cache=shared')
# Test sqlite3.connect(':memory:?cache=private')
# Test sqlite3.connect(':memory:?cache=shared', uri=True)
# Test sqlite3.connect(':memory:?cache=private', uri=True)
# Test sqlite3.connect('file:memory:?cache=shared', uri=True, check_same_thread=False)
# Test sqlite3.connect('file:memory:?cache=private', uri=True, check_same_thread=False)
# Test sqlite3.connect(':memory:?cache=shared', uri=True, check_same_thread=False)
# Test sqlite3.connect(':memory
