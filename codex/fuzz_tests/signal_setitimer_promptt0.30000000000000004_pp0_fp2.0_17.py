import signal
# Test signal.setitimer() and signal.getitimer()

import time
import unittest
from test import support

class TestItimer(unittest.TestCase):

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)
        self.old_itimer = signal.getitimer(signal.ITIMER_REAL)
        self.alarm_received = False

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)
        signal.setitimer(signal.ITIMER_REAL, *self.old_itimer)

    def alarm_handler(self, signum, frame):
        self.alarm_received = True

    def test_itimer(self):
        # test that the timer fires
        signal.setitimer(signal.ITIMER_REAL, 0.1, 0)
        time.sleep(0.2)
        self.assertTrue(self.alarm_received)

       
