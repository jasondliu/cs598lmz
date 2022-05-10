import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with timeout, in a separate thread.
#
# This function is called from Python code, once for each thread.
#
# The function starts a separate thread that blocks on sqlite3.connect().
# The main thread then calls sqlite3.thread_cleanup() to interrupt all
# SQLite operations.  This causes the thread to raise an exception, which
# is detected by the Python code.
#
# The thread_id is used as the name of the lock/semaphore file.
def connect_with_timeout(dbname, timeout):
    lockfile = "/tmp/test-timeout.%d" % threading.get_ident()
    try:
        os.unlink(lockfile)
    except OSError:
        pass

    def test_thread():
        try:
            os.open(lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
        except OSError:
            return False
        try:
            sqlite3.connect(":memory:", timeout=timeout)
        except sqlite3.Operational
