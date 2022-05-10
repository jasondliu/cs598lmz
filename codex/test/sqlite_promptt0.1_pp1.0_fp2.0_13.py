import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

# This is a test of the sqlite3 module.  It is not a complete test.
# It does not test the ability to define new aggregate, collating,
# or function callbacks from Python.

# The tests are defined in a class called SQLiteTest.  There is a
# subclass for each supported database API.  The base class contains
# code to open and close the database, create tables, and define
# utility functions.  The subclasses define test cases.

# The test cases are defined with methods whose names start with
# 'test_'.  The 'test_' prefix is stripped off to define the test
# number.  For example, 'test_create_table' is test 1.

# The test cases are run in increasing order by test number.  If a
# test fails, the remaining tests are not run.

# The test cases are run in a separate thread.  The main thread
# watches for output on stdout or stderr.  If any output is produced,
# the test fails.  This is to catch print statements that are executed

