import signal
# Test signal.setitimer.

import time
import unittest

from test import support
threading = support.import_module('threading')

class TestSetitimer(unittest.TestCase):
    def setUp(self):
        self.ran = False
        self.signalled = False

    def handler(self, signum, frame):
        self.signalled = True

    def test_setitimer(self):
        # Test that the timer fires in roughly the right amount of time.
        signal.signal(signal.SIGALRM, self.handler)
        signal.setitimer(signal.ITIMER_REAL, 0.1)
        time.sleep(0.2)
        self.assertTrue(self.signalled)

    def test_setitimer_cancel(self):
        # Test that cancelling the timer works.
        signal.signal(signal.SIGALRM, self.handler)
        signal.setitimer(signal.ITIMER_REAL, 0.1)
        time.sleep(0.2)
        signal
