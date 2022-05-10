import signal
# Test signal.setitimer
#
# This test is not run by default.  To run it, do:
#
#   python test_signal.py -u network
#
# The test will fail if the system does not support setitimer.

import os
import sys
import time
import unittest
from test import support

try:
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
except AttributeError:
    raise unittest.SkipTest("system doesn't support setitimer")

class AlarmTest(unittest.TestCase):
    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

