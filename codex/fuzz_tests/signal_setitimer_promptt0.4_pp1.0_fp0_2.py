import signal
# Test signal.setitimer
#
# This test is a little more complicated than the other setitimer tests
# because it checks that the timer is reset when the handler is called.
#
# This test must be run with a shell that supports the "time" command.

import os
import signal
import sys
import time
import unittest

from test import support

# On Windows, the timer resolution is 10-15ms, so we need to allow
# for that.
TIMER_RESOLUTION = 0.01

class TestSetitimer(unittest.TestCase):
    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)
        self.alarm_count = 0

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

    def alarm_handler(self, signum, frame):
        self.alarm_count += 1

    def test_setitimer_basic(self):
        # Check that setitimer() works.

