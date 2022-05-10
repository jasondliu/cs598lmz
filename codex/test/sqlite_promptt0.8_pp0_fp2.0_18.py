import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:").command_line()
assert sqlite3.connect(":memory:").command_line()

# Test for a known good version of sqlite3
# We have to dynamically do this because the sqlite3 library version
# is not tied directly back to the version of the python sqlite3 module
# It should be in most cases but there is nothing in the sqlite3 code
# to guarantee it.
# Looking at the output of sqlite3.version, sqlite3.sqlite_version and
# sqlite3.sqlite_version_info it looks like the sqlite_version_info
# part of the version string is the version that the python module
# is compiled against.  So we should be ok but we check just in case.
sqlite_version = 3.6
libname = ctypes.util.find_library('sqlite3')
if libname:
    lib = ctypes.CDLL(libname)
