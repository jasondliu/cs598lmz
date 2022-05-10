import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
# Test sqlite3.connect('file:memory:?cache=private', uri=True)

# Test sqlite3.connect(':memory:', uri=True)
# Test sqlite3.connect('file::memory:?cache=shared', uri=True)
# Test sqlite3.connect('file::memory:?cache=private', uri=True)

# Test sqlite3.connect('file:?cache=shared', uri=True)
# Test sqlite3.connect('file:?cache=private', uri=True)

# Test sqlite3.connect('file:?mode=memory&cache=shared', uri=True)
# Test sqlite3.connect('file:?mode=memory&cache=private', uri=True)

# Test sqlite3.connect('file::memory:?cache=shared', uri=True)
# Test sqlite3.connect('file::memory:?cache=private', uri=True)

# Test sqlite3.connect('file
