import signal
# Test signal.setitimer
#
# This test is not very good, because it relies on the timer
# expiring at the right time.  If the test is run on a heavily
# loaded system, the timer may expire later than expected.
#
# Written by Bill Tutt.  Public Domain.

import unittest
import sys
import time

from test import support

# This test is not very good, because it relies on the timer
# expiring at the right time.  If the test is run on a heavily
# loaded system, the timer may expire later than expected.

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

class ItimerTest(unittest.TestCase):
    def setUp(self):
        self.old_alarm_handler = signal.signal(signal.SIGALRM, alarm_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm_handler)

    def test_itimer_zero(self):
        # Test that itimer
