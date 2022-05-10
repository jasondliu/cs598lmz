import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect with a timeout.
#
# 1. Create a new database with a table.
# 2. Create a thread that will take a long time to insert a row into the table.
# 3. Open the database, but set a timeout for the query.
# 4. Join the thread.
# 5. If the test fails, the thread will never complete and we will timeout.
#
# The timeout should be less than the time it takes for the thread to insert
# the row.
#
# This test has been observed to fail when the system is under load and the
# timeout is around 1 second. However, the timeout is a lower bound and not
# an upper bound, and so the timeout should be shorter than the time it takes
# to insert the row.
#
# This test has been observed to fail on Android with a timeout of 0.3 seconds
# when the test is run in isolation, but not when it is run as part of a suite.

# Create a new database with a table.
conn = sqlite3.connect(':memory:')
conn.execute('create table test (x)')
conn.commit()

#
