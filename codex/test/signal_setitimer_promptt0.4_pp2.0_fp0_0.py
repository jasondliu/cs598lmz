import signal
# Test signal.setitimer() and signal.getitimer()

import sys
import time
import unittest
from test.support import run_unittest, import_module, cpython_only

# Test signal.setitimer() and signal.getitimer()

class ItimerTest(unittest.TestCase):
    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

    def alarm_handler(self, signum, frame):
        self.fail("SIGALRM received")

    def test_itimer_zero(self):
        # Test setting an itimer to zero.
        signal.setitimer(signal.ITIMER_REAL, 0)
        self.assertEqual(signal.getitimer(signal.ITIMER_REAL), (0.0, 0.0))

