import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect in a thread
#
# This is a test to see if sqlite3.connect works in a thread if the
# sqlite3 library is loaded by ctypes.
#
# The test is to create a thread and have it open and close a database
# connection.  This is repeated a number of times.

# The test is run in two different ways:
#
# 1. The sqlite3 library is loaded by ctypes.
# 2. The sqlite3 library is loaded by the sqlite3 module.

# When the sqlite3 library is loaded by ctypes, the test hangs.
# When the sqlite3 library is loaded by the sqlite3 module, the test
# completes without hanging.

# The test is run a number of times, and the probability of it hanging
# when the sqlite3 library is loaded by ctypes is about 1/3.  When it
# hangs, it hangs on the call to sqlite3_close.
#
# I'm running Mac OS X 10.5.6, Python 2.5.1, sqlite3-3.3.6,
# sqlite-3
