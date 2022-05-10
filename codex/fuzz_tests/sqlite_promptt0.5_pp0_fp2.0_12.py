import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#
# NOTE: This test is not run by default.
#
# This test is designed to be run in a separate process.  It is
# not run by default because it takes a long time to run and it
# doesn't do anything useful.
#
# The test is designed to test sqlite3.connect() under extreme
# stress.  It is intended to flush out any bugs in the
# pysqlite2.dbapi2.Connection constructor and the
# sqlite3_open_v2() interface.
#
# To run the test, start a Python interpreter in this directory and
# type:
#
#   >>> import test_stress
#   >>> test_stress.test()
#
# The test will run for a long time and print periodic progress
# updates to stderr.
#
# If the test completes without raising an exception, it has
# passed.  If the test raises an exception, the test has failed.

# Try to load the sqlite3 module.  If it is not available, skip this
# test.
try:
    import sqlite3
except ImportError
