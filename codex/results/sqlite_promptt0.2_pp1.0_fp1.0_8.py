import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)

# This is a test of the sqlite3 module.  The goal is to cover all of the
# public C API, through either direct calls to sqlite3_* methods, or by
# going through the Python sqlite3 module.

# This test does NOT test the Python sqlite3.dump module.  That is tested
# in test_dump.py.

# The tests are defined in TestSQLite.test_list.  The test_list is a list
# of tuples.  Each tuple has the following format:
#
#       ( title,                          # Title of the test
#         [ sql statements ],             # List of SQL statements to run
#         [ list of tuples for .fetchall() output ]
#         { dict of name:value substitutions for use in SQL }
#         )
#
# The substitutions are useful for testing the same SQL statement with
# different parameters.  For example, the SQL statement
#
#       SELECT :x
#
# can be tested with x=1
