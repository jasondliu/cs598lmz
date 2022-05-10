import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.set_trace_callback

# Code to test the feature.

# The database connection object.
conn = None

# The trace callback.
