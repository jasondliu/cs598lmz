import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# sqlite3.connect()

# sqlite3.connect(database[, timeout, detect_types, isolation_level, check_same_thread, factory, cached_statements, uri])

# Open a connection to the SQLite database file database. You can use ":memory:" to open a database connection to a database that resides in RAM instead of on disk.

# database
# The database name.

# timeout
# Timeout value in seconds to use for the connection. The default value is 5.0 seconds.

# detect_types
# This parameter can be set to a custom type conversion function.

# isolation_level
# None or one of "DEFERRED", "IMMEDIATE", or "EXCLUSIVE".

# check_same_thread
# If set to True, the sqlite3 module verifies that connections are not shared across threads. This check significantly slows down connection creation.

# factory
# This parameter can be set to a custom row factory.

# cached_statements
# This parameter can be set to a positive integer to enable the use of a statement cache.


