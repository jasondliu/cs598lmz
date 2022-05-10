import signal
# Test signal.setitimer() with alarm()
#
# This test is skipped if the system doesn't support itimer
#
import os
import sys
import time
import unittest

from test import support

if not hasattr(signal, "setitimer"):
    raise unittest.SkipTest("platform doesn't support itimer")

class AlarmTestCase(unittest.TestCase):

    def setUp(self):
        self.oldalarm = signal.signal(signal.SIGALRM, self.handler)
        signal.setitimer(signal.ITIMER_REAL, 0)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.oldalarm)

    def handler(self, signum, frame):
        self.alarm_fired = 1

    def test_alarm(self):
        self.alarm_fired = 0
        signal.alarm(1)
        time.sleep(2)
        self.assertTrue(self.alarm_fired)

