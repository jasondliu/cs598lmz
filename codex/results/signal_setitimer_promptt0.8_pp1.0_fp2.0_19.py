import signal
# Test signal.setitimer.

from test.test_support import verify, verbose, run_unittest

from signal import setitimer, ITIMER_REAL, ITIMER_VIRTUAL, ITIMER_PROF, \
                   ITIMER_REALPROF, SIGALRM

import time

VERIFY_INTERVAL=0.25

def alarm_handler(signum, frame):
    print 'got SIGALRM'

class AlarmTest(unittest.TestCase):

    def setUp(self):
        self.old_alarm_handler = signal.signal(SIGALRM, alarm_handler)

    def tearDown(self):
        signal.signal(SIGALRM, self.old_alarm_handler)

    def verify_interval(self, interval):
        """Verify that the interval is within expected bounds."""
        elapsed = time.time() - self.start
        if verbose:
            print 'elapsed =', elapsed, '; interval =', interval
        # Interval should be within 70% .. 130% of the expected value
