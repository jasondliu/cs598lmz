import signal
# Test signal.setitimer
#
# This test is Linux-specific.

import os, time
import unittest
from test.support import run_unittest, reap_children, get_attribute

# Skip this test if setitimer() is not available.
requires_setitimer = unittest.skipUnless(hasattr(signal, 'setitimer'),
                                         'requires setitimer()')

@requires_setitimer
class SetitimerTest(unittest.TestCase):

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

    def alarm_handler(self, signum, frame):
        self.alarm_fired = True

    def test_setitimer(self):
        self.alarm_fired = False
        signal.setitimer(signal.ITIMER_REAL, 0.1)
