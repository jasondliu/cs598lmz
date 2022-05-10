import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)
# Test sqlite3.connect('file:memdb1?cache=shared', uri=True)
# Test sqlite3.connect('file:memdb1?mode=memory', uri=True)
# Test sqlite3.connect('file:memdb1', uri=True)

# Test sqlite3.connect(':memory:?cache=shared')
# Test sqlite3.connect(':memory:')

# Test sqlite3.connect('file:memdb2?mode=memory&cache=shared', uri=True)
# Test sqlite3.connect('file:memdb2?cache=shared', uri=True)
# Test sqlite3.connect('file:memdb2?mode=memory', uri=True)
# Test sqlite3.connect('file:memdb2', uri=True)

# Test sqlite3.connect(':memory:?cache=shared')
# Test sqlite3.connect(':memory:')

# Test sqlite3.
