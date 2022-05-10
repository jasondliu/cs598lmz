import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.total_changes
#
# The following code runs the test twice in two threads, in separate
# interpreters, and checks that the changes are visible in both.
#
# This test requires a new sqlite3 library built with SQLITE_THREADSAFE=1
# (the default).  It also requires the standard library threading module.
#
# XXX Note that this test and test_dbapi_threads.py should be
# intermingled.

# Create a database with three tables, each with a single column, "n".
# Fill the table with 10 rows each: (0,), (1,), ..., (9,).
#
# Make a thread that increments one row in each table, in a loop:
#   UPDATE tbl SET n = n + 1 WHERE n = 0
# Make a main thread that does the same, but for n = 3.
#
# After each UPDATE, check that total_changes in both threads is correct.
#
# Every 1 second, in both threads, check that total_changes is correct.

to_the_main_thread = []
from_the_main
