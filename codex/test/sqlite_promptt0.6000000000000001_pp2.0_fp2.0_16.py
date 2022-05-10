import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

import _ctypes
import sip

def test_threading():
    """
    Test that the threading module works.  Note that the test is
    deliberately incomplete, because there are a number of issues with
    threading, which are not currently fixed.  Specifically, the
    test_threading_local.py test module has been removed because the
    test was too fragile.

    There is also a problem with Python's implementation of
    threading.Condition.notifyAll(), which can cause a deadlock.
    """

    # Create a thread and wait for it to finish.
    def threadproc():
        pass

    thread = threading.Thread(target=threadproc)
    thread.start()
    thread.join()

    # Create a thread and wait for it to finish, then create a second
    # thread and wait for it to finish.
    thread = threading.Thread(target=threadproc)
    thread.start()
    thread.join()

    thread = threading.Thread(target=threadproc)
    thread.start()
    thread.join()

