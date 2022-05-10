import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect C API with a multithreaded Python program.

# The C API is thread-safe because each sqlite* handle is thread-specific.
# In other words, the handle is not shared across threads, and each
# thread gets a different handle each time it calls sqlite3_open().

# But if using a custom sqlite3.connect() implementation that passes a
# shared handle to the parent sqlite3 module, then the SQLite library
# is no longer thread-safe at all.

# Note: This code only demonstrates the problem. It is not a proper
#       regression test with a test case for each reported bug.

# This test case is based on one reported by Christian Hammond:
# http://bugs.python.org/issue15486
# And another by Manuel Jacob:
# http://bugs.python.org/issue6161

# Some thread states, for debugging purposes only.
THREAD_WAITING = 0
THREAD_WORKING = 1
THREAD_DONE = 2

def log(msg, *args):
    print(msg % args)

