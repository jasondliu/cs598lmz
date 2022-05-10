import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() function
[sqlite3.connect(filename) for filename in [':memory:', 'file:memory:?cache=shared']]

# <sqlite3.Connection at 0x7f930c07ee20>
# <sqlite3.Connection at 0x7f930c07eea0>
# ... and the underlying sqlite3 handle
sqlite3.connect(':memory:').execute('select sqlite3_version(), sqlite3_memory_used(), sqlite3_memory_highwater(1)').fetchall()

# [(u'3.32.3', 359, 599), (u'3.32.3', 359, 599)]

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
print("{:12} {}".format("SQLite", lib.sqlite3_sourceid()))
