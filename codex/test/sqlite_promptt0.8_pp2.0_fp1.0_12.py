import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() behavior with threading.Lock().

# sqlite3.connect() is wrapped in a lock to prevent
# multiple threads from trying to create a sqlite3
# connection at the same time.
_connect_lock = threading.Lock()

# The OS-level locking implementation may not be within the
# Python interpreter, so the lock may not be reentrant.
#
# If the OS-level implementation is within the Python interpreter
# (as in BSD), a reentrant lock will be used.
#
# If the OS-level implementation calls into the C library
# (as in Linux), a non-reentrant lock will be used.
_is_reentrant = not hasattr(ctypes, 'pythonapi')

if _is_reentrant:
    class ReentrantLock(threading.RLock):
        is_reentrant = True
else:
    class ReentrantLock(threading.Lock):
        is_reentrant = False

