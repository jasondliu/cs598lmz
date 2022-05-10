import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)

# See: https://www.sqlite.org/sharedcache.html
# See: https://stackoverflow.com/questions/8546541/how-to-use-sqlite-shared-cache-in-python

# See: https://github.com/mackyle/sqlite/blob/master/src/dbapi2.c

# SQLITE_OPEN_SHAREDCACHE = 0x00040000
# SQLITE_OPEN_FULLMUTEX = 0x00010000
# SQLITE_OPEN_PRIVATECACHE = 0x00080000
# SQLITE_OPEN_URI = 0x00000040
# SQLITE_OPEN_NOMUTEX = 0x00008000
# SQLITE_OPEN_READWRITE = 0x00000002

# SQLITE_OPEN_READONLY = 0x00000001

# SQLITE_OPEN_MAIN_DB = 0x00000100
# SQLITE_OPEN_TEMP
