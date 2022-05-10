import signal
# Test signal.setitimer() on all supported platforms.
import sys
import time
import unittest
from test.support import os_helper

verbose = False

def handler(*args):
    raise KeyboardInterrupt

def handler_set_errno(*args):
    os.write(2, b"handler_set_errno called\n")
    errno = ctypes.get_errno()
    if verbose:
        sys.stderr.write("handler_set_errno setting errno to %d\n" % errno)
    new_errno = errno + 1
    ctypes.set_errno(new_errno)
    if verbose:
        sys.stderr.write("handler_set_errno exiting, errno: %d\n" %
                         ctypes.get_errno())

class ItimerTest(unittest.TestCase):

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, handler)
        self.old_errno = ctypes.get_err
