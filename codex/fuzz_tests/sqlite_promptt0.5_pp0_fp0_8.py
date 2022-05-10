import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('/tmp/test.db')
# Test sqlite3.connect('file::memory:?cache=shared')
# Test sqlite3.connect('file:/tmp/test.db?mode=ro', uri=True)
# Test sqlite3.connect('file:/tmp/test.db?mode=rw', uri=True)
# Test sqlite3.connect('file:/tmp/test.db?mode=rwc', uri=True)
# Test sqlite3.connect('file:/tmp/test.db?mode=memory', uri=True)
# Test sqlite3.connect('file:/tmp/test.db?mode=memory&cache=shared', uri=True)
# Test sqlite3.connect('file::memory:?cache=shared', uri=True)
# Test sqlite3.connect('file::memory:?mode=memory&cache=shared', uri=True)
# Test sqlite3.connect('file::memory:?mode=memory', uri=True)
# Test sqlite3.connect
