import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('file:memory:')
# Test sqlite3.connect('file::memory:')
# Test sqlite3.connect('file::memory:?cache=shared')

# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared')
# Test sqlite3.connect('file:memdb1?mode=memory&cache=private')
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared&psow=1')
# Test sqlite3.connect('file:memdb1?mode=memory&cache=private&psow=1')

# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared&psow=0')
# Test sqlite3.connect('file:memdb1?mode=memory&cache=private&psow=0')

# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared&psow=1&nolock=1')
# Test sqlite3.connect('
