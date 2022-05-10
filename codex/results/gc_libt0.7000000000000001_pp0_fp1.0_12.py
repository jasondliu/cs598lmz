import gc, weakref

import _thread
import threading
import _testcapi
import time
import os
import sys
import unittest
import subprocess
import warnings

# We need to have a threading.Thread object in order to test
# _thread._count(), so just create a dummy one.
THREAD_DUMMY = threading.Thread()

# Don't use support.threading_setup() since _thread isn't
# an implicit import.
import _thread
_thread.threading_setup()

# Disable the tests if the implementation doesn't support it.
requires_threads = unittest.skipUnless(threading, 'Threading required for this test.')
requires_threads._maxDiff = None

# Some tests need a resource that only allows one thread at a time.
_threading_test_lock = _thread.allocate_lock()

# Basic test for thread module

def _threading_test():
    # This function runs in a separate thread.
    with _threading_test_lock:
        ident = _thread.get_ident()
    time.sleep
