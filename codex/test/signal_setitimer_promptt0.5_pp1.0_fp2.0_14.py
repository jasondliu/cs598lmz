import signal
# Test signal.setitimer() and signal.getitimer()

import time
import unittest
from test.support import run_unittest

class TimerTest(unittest.TestCase):

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)
        self.old_itimer = signal.getitimer(signal.ITIMER_REAL)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)
        signal.setitimer(signal.ITIMER_REAL, *self.old_itimer)

    def alarm_handler(self, signum, frame):
        self.alarm_fired = True

    def test_itimer_zero(self):
        signal.setitimer(signal.ITIMER_REAL, 0, 0)
        time.sleep(0.1)
        self.assertFalse(self.alarm_fired)

