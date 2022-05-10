import signal
# Test signal.setitimer.

import unittest
from test.support import run_unittest


class SetitimerTest(unittest.TestCase):

    def itimer_signal_handler(self, signum, frame):
        if signum == signal.SIGALRM:
            self.alarm_caught = 1

    # Test signal delivery.  There should be at least one timer
    # expiry during this sleep .
    def test_itimer_signal(self):
        self.alarm_caught = 0
        signal.signal(signal.SIGALRM, self.itimer_signal_handler)
        signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
        time.sleep(1)
        self.assertNotEqual(self.alarm_caught, 0)

    # Test return values from setitimer.
    def test_itimer_return(self):
        old_timer = signal.setitimer(signal.ITIMER_REAL, 1, 2)
