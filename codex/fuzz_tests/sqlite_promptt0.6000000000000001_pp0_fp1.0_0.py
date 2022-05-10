import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect in other thread

# https://github.com/python/cpython/blob/master/Modules/_sqlite/cursor.c
# https://www.sqlite.org/c3ref/intro.html

# sqlite3_open()

# The first parameter is the filename for the database. If it does not exist,
# a new one is created.
# The second parameter is the flags.
# SQLITE_OPEN_READONLY
#       Open the database for reading only.
# SQLITE_OPEN_READWRITE
#       Open the database for reading and writing.
# SQLITE_OPEN_CREATE
#       Create the database if it does not already exist.
# SQLITE_OPEN_URI
#       Interpret the filename as a URI if true.
# SQLITE_OPEN_MEMORY
#       Open a database connection to a database that resides in RAM instead of on disk.
# SQLITE_OPEN_NOMUTEX
#       The database connection opens in the multi-thread threading mode as long as
#       the single-thread mode has not been set
