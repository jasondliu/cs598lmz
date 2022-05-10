import signal
# Test signal.setitimer()
#
# This test is not very thorough, but it does exercise the code.
#
# Note:  This test is known to fail on some platforms.
#
# XXX This test is known to fail on some platforms.
# XXX It is disabled for now.

import unittest
from test import support

class SetitimerTest(unittest.TestCase):

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)
        self.alarm_received = False

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

    def alarm_handler(self, signum, frame):
        self.alarm_received = True

    def test_setitimer(self):
        # Test that setitimer() works.
        signal.setitimer(signal.ITIMER_REAL, 0.1)
        support.get_attribute(self, 'alarm_received')
        self.assertTrue(self.
