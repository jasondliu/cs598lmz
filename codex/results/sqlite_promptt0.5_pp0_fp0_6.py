import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('/tmp/test.db')

# Test sqlite3.connect('file:memory:')
# Test sqlite3.connect('file:/tmp/test.db')

# Test sqlite3.connect('file::memory:')
# Test sqlite3.connect('file:test.db')

# Test sqlite3.connect('file::memory:?cache=shared')
# Test sqlite3.connect('file:test.db?cache=shared')

# Test sqlite3.connect('file::memory:?cache=private')
# Test sqlite3.connect('file:test.db?cache=private')

# Test sqlite3.connect('file::memory:?cache=shared&mode=ro')
# Test sqlite3.connect('file:test.db?cache=shared&mode=ro')

# Test sqlite3.connect('file::memory:?cache=private&mode=ro')
# Test sqlite3.connect('file:test.db?cache=private&mode=ro')

# Test
