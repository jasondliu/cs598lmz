import signal
# Test signal.setitimer() and signal.alarm()
import sys
import threading
import time
import unittest
from test import support

try:
    signal.alarm
except AttributeError:
    raise unittest.SkipTest("signal.alarm not defined")


def handler1(*args):
    pass


def handler2(*args):
    pass


@unittest.skipUnless(hasattr(signal, 'setitimer'), 'need signal.setitimer()')
class ItimerTest(unittest.TestCase):
    # Issue #11647: itimer() must not be interrupted by a signal handler
    # raising an exception.
    @support.reap_threads
    def test_setitimer_interrupted(self):
        # If a signal handler for SIGALRM raises an exception, the itimer()
        # call must not be interrupted.
        def raise_in_handler(signum, frame):
            raise KeyboardInterrupt
        signal.signal(signal.SIGALRM, raise_in_handler)
        self.assertRaises(KeyboardInterrupt
