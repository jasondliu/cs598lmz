import signal
# Test signal.setitimer() and signal.getitimer().

import time
import unittest

from test import support

# Skip if setitimer() does not exist.
support.get_attribute(signal, 'setitimer')

# Skip if getitimer() does not exist.
support.get_attribute(signal, 'getitimer')

class SignalAlarm(unittest.TestCase):
    def setUp(self):
        self.oldalarm = signal.signal(signal.SIGALRM, self.handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.oldalarm)

    def handler(self, signum, frame):
        self.fired = True

    def test_itimer_zero(self):
        # Issue #10803: setitimer() should not segfault with an invalid
        # interval
        with self.assertRaises(ValueError):
            signal.setitimer(signal.ITIMER_REAL, 0, -1)

