import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
# Test sqlite3.connect('file:memory:?cache=private', uri=True)
# Test sqlite3.connect('file:memory:?cache=shared', uri=True).executemany()
# Test sqlite3.connect('file:memory:?cache=private', uri=True).executemany()
# Test sqlite3.connect('file:memory:?cache=shared', uri=True).executescript()
# Test sqlite3.connect('file:memory:?cache=private', uri=True).executescript()
# Test sqlite3.connect('file:memory:?cache=shared', uri=True).cursor()
# Test sqlite3.connect('file:memory:?cache=private', uri=True).cursor()
# Test sqlite3.connect('file:memory:?cache=shared', uri=True).cursor().executemany()
# Test sqlite3.connect('file:memory:?cache=private', uri=True).c
