import signal
# Test signal.setitimer()

# This test is known to fail on some systems.
# If you have a system where this test fails,
# please report it to the Python bug tracker.

import signal
import unittest
from test import support

class ItimerTest(unittest.TestCase):

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)
        self.alarm_flag = False

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

    def alarm_handler(self, signum, frame):
        self.alarm_flag = True

    def test_itimer_zero(self):
        signal.setitimer(signal.ITIMER_REAL, 0, 0)
        self.assertEqual(signal.getitimer(signal.ITIMER_REAL), (0.0, 0.0))
        self.assertFalse(self.alarm_flag)

    def test_itimer_
