import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared')

# Test sqlite3.connect('/home/james/sqlite/test.db')
# Test sqlite3.connect('/home/james/sqlite/test.db?cache=private')

# Test sqlite3.connect('/home/james/sqlite/test.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
# Test sqlite3.connect('/home/james/sqlite/test.db', check_same_thread=False)

# Test sqlite3.connect('/home/james/sqlite/test.db', uri=True)

# Test sqlite3.connect('file:/home/james/sqlite/test.db?mode=ro', uri=True)

# Test sqlite3.connect('file:/home/james/sqlite/test.db?mode=ro', uri=True, check_same
