import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.set_trace_callback

# Code to test the feature.

# The database connection object.
conn = None

# The trace callback.
def trace(sql):
    print "SQL:", sql

# The callback used for timing out the test.
def timeout():
    print "Timed out!"
    global conn
    conn.close()

# The callback used for testing the database connection.
def test():
    print "Testing!"
    global conn
    conn = sqlite3.connect(":memory:")
    conn.set_trace_callback(trace)
    conn.execute("SELECT 1")
    conn.execute("SELECT 2")
    conn.close()

# Set up the timer.
t = threading.Timer(5.0, timeout)
t.start()

# Perform the test.
test()

# Cancel the timer.
t.cancel()
