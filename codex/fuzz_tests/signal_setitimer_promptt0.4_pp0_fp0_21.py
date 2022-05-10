import signal
# Test signal.setitimer() and signal.getitimer()

import time
import unittest
from test import support

class ItimerTest(unittest.TestCase):

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)
        self.old_itimer = signal.getitimer(signal.ITIMER_REAL)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)
        signal.setitimer(signal.ITIMER_REAL, *self.old_itimer)

    def alarm_handler(self, signum, frame):
        pass

    def test_getitimer(self):
        # Test getitimer()
        self.assertEqual(signal.getitimer(signal.ITIMER_REAL), (0.0, 0.0))
        signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)
        self.assertE
