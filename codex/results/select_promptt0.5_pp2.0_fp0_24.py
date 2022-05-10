import select
# Test select.select with a non-socket object
import os
import select
import sys
import threading
import time
import unittest
import warnings
import weakref
import socket
import errno
import gc

from test.support import (threading_helper,
                          run_unittest, reap_threads,
                          unlink)

try:
    import resource
except ImportError:
    resource = None

threading.stack_size(4096)

#
# Test utility to run a function in a sub-thread, and time out in case
# the thread doesn't complete.
#

def threading_setup():
    # Just in case the whole test fails, let's not leak threads
    reap_threads()

def threading_cleanup():
    # Just in case the whole test fails, let's not leak threads
    reap_threads()

class ThreadedFunction:
    def __init__(self, t, e, v, f, args, kwargs):
        self.t = t
        self.e = e
        self.v = v
