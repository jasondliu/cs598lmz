import signal
# Test signal.setitimer
#
# This test is a bit tricky because we want to test that the signal is
# delivered at the right time, but we don't want to wait for the timer to
# expire.  We use a signal handler that sets an event, and we use
# select.select with a timeout to wait for the event to be set.

import select
import signal
import time
import unittest
from test import support

# Some platforms can't set itimer intervals less than 1 second.
MIN_INTERVAL = getattr(signal, 'ITIMER_MIN', 1)

def handler(*args):
    got_signal.set()

class ItimerTest(unittest.TestCase):
    def setUp(self):
        self.old_handler = signal.signal(signal.SIGALRM, handler)
        self.addCleanup(signal.signal, signal.SIGALRM, self.old_handler)
        self.old_itimer_interval = signal.setitimer(signal.ITIMER_REAL, 0)
