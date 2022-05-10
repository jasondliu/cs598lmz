import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

# This is a test of the sqlite3 module.  It is not a complete test.
# It does not test the ability to define new aggregate, collating,
# or functions.  It does not test the ability to define new types.
# It does not test the ability to use the database in WAL mode.
# It does not test the ability to use the database in shared cache mode.
# It does not test the ability to use the database in multi-thread mode.
# It does not test the ability to use the database in multi-process mode.
# It does not test the ability to use the database with a memory-mapped file.
# It does not test the ability to use the database with a read-only file.
# It does not test the ability to use the database with a read-only memory buffer.
# It does not test the ability to use the database with a memory buffer.
# It does not test the ability to use the database with a file descriptor.
# It does not test the ability to use the database with a file-like object.
# It does not test the ability
