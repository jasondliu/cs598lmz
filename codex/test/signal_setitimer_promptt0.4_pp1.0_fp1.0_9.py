import signal
# Test signal.setitimer() and signal.getitimer()
#
# XXX This test is known to fail on FreeBSD 4.x, but it's not clear
# whether the problem is in the test or in the implementation.

import time
import unittest

from test import support

class TimeIt(unittest.TestCase):

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

    def handler(self, signum, frame):
        self.triggered = 1

    def test_itimer_zero(self):
        # Test setting itimer to zero.
        self.triggered = 0
        signal.setitimer(signal.ITIMER_REAL, 0)
        time.sleep(0.1)
        self.assertEqual(self.triggered, 0)
        signal.setitimer(signal.ITIMER_REAL, 0)
       
