import signal
# Test signal.setitimer() on SIGVTALRM.
import time
import unittest
import sys

from test import support

is_jython = sys.platform.startswith('java')

class TestSignal(unittest.TestCase):

    def setUp(self):
        # Save previous alarm handler and alarm value
        self.old_alarm = signal.signal(signal.SIGALRM, signal.SIG_IGN)
        self.old_itimer_num, self.old_itimer_denom = signal.getitimer(signal.ITIMER_REAL)

    def tearDown(self):
        # Restore previous alarm handler and alarm value
        signal.signal(signal.SIGALRM, self.old_alarm)
        signal.setitimer(signal.ITIMER_REAL, self.old_itimer_num,
                         self.old_itimer_denom)

    def _wait_for_alarm(self, secs):
        # Wait for the alarm to go off.
        time.sleep(secs + 1)
