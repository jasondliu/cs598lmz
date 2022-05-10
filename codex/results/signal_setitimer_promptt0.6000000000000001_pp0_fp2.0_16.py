import signal
# Test signal.setitimer() and signal.getitimer().

from test.support import verbose, run_with_locale
import time
import unittest
from test import support


class Timeit(unittest.TestCase):

    def setUp(self):
        self.old_alarm_handler = signal.signal(signal.SIGALRM, self.alarm_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm_handler)
        if verbose:
            print('\n', end=' ')

    def alarm_handler(self, signum, frame):
        raise OSError("got signal %s" % signum)

    def test_setitimer(self):
        if verbose:
            print('setitimer()')

        # Test setting the timer for 0, and then resetting it for
        # a longer period.
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.setitimer(signal.ITIMER_REAL,
