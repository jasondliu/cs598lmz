import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with a timeout value
#
# The test case should:
# - use a timeout that is too short
# - open a database file (that does not exist)
# - the open should fail with an exception
# - the exception should be an OperationalError
# - the exception should have a .timeout attribute set to True
#
# If the timeout works, the test should complete in less than one second.
#

# Set up a test file that does not exist.
#
dbfile = tempfile.mktemp()

# Set up a timeout in seconds
#
timeout = 1.0

# Set up the connection.
#
conn = sqlite3.connect(dbfile, timeout=timeout)

start = time.time()

try:
    # This call should fail with an exception
    #
    cur = conn.cursor()

finally:
    stop = time.time()
    elapsed = stop - start
    #print 'Elapsed:', elapsed


# Check that the exception object is an OperationalError
#
#assert isinstance(e, sqlite3.OperationalError
