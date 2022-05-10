import signal
# Test signal.setitimer() and signal.getitimer()
#
# This test is Linux-specific.

import os
import sys
import time
import unittest


class TestItimer(unittest.TestCase):

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_received)
        signal.setitimer(signal.ITIMER_REAL, 0)

    def tearDown(self):
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, self.old_alarm)

    def alarm_received(self, sig, frame):
        self.fail("SIGALRM received")

    def test_getitimer(self):
        self.assertEqual(signal.getitimer(signal.ITIMER_REAL), (0.0, 0.0))
        signal.setitimer(signal.ITIMER_REAL, 1.3, 0.7)
