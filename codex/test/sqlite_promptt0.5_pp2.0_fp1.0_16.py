import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

#
# Try to load the sqlite3 module.
#
try:
    from sqlite3 import dbapi2 as sqlite
except ImportError:
    print("WARNING: sqlite3 module not found. Attempting to load sqlite2.")
    from pysqlite2 import dbapi2 as sqlite

#
# Try to load the sqlite3 module.
#
try:
    from sqlite3 import dbapi2 as sqlite
except ImportError:
    print("WARNING: sqlite3 module not found. Attempting to load sqlite2.")
    from pysqlite2 import dbapi2 as sqlite

#
# Try to load the ctypes module.
#
try:
    import ctypes
except ImportError:
    print("WARNING: ctypes module not found. Shared cache will not work.")

#
# Try to load the sqlite3 module.
#
