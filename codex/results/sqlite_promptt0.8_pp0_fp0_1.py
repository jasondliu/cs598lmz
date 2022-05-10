import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/sdcard/sqlite_stmt_journals/foo")
import sys
import android_equake_plot

lib = ctypes.CDLL("libsqlite3.so")

# sqlite3_initialize();
lib.sqlite3_initialize()

# # This function returns the number of times that the busy callback has
# # been invoked for the current SQL statement.
# #
# # If no busy callback was defined or if the database connection is
# # closed before this function is called, then zero is returned.
# #
# int sqlite3_busy_handler(sqlite3*, int(*)(void*,int), void*);
def callback(p, count):
    print "callback", p, count
    return count
busy_handler = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(callback)

# # Execute SQL code.  Return a result set object if the given statement
# # returns data, or None otherwise.
# #
# # By default, the database module
