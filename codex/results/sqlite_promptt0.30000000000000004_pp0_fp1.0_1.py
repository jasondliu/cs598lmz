import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared')
# Test sqlite3.connect('file:memdb1?mode=memory&cache=private')
# Test sqlite3.connect('file:memdb1?cache=shared')
# Test sqlite3.connect('file:memdb1?cache=private')
# Test sqlite3.connect('file:memdb1?mode=memory')
# Test sqlite3.connect('file:memdb1')

# Test sqlite3.connect(':memory:')

# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)
# Test sqlite3.connect('file:memdb1?mode=memory&cache=private', uri=True)
# Test sqlite3.connect('file:memdb1?cache=shared', uri=True)
# Test sqlite3.connect('file:memdb1?cache=private', uri=True)
# Test sqlite3.connect('file:memdb1?mode=memory', uri=True)
#
