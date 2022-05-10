import signal
# Test signal.setitimer() on a signal that is not ignored or caught.
# Check that EINVAL is raised when the interval is negative.
import time
import unittest

from test.support import run_unittest, captured_output


@unittest.skipUnless(hasattr(signal, 'setitimer'), 'requires setitimer()')
class SetitimerTest(unittest.TestCase):

    def setUp(self):
        self.received = False

    def handler(self, signum, frame):
        self.received = True

    def test_setitimer(self):
        self.assertRaises(ValueError, signal.setitimer, -1, 0)
        self.assertRaises(ValueError, signal.setitimer, signal.NSIG, 0)
        self.assertRaises(ValueError, signal.setitimer, signal.SIGUSR1, -0.1)
        signal.signal(signal.SIGUSR1, self.handler)
        signal.setitimer(signal.ITIMER_REAL, 0.2, 0
