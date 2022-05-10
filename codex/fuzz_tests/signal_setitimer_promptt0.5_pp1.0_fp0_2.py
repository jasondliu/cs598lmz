import signal
# Test signal.setitimer

import time
import unittest
from test import support

# Set up a signal handler that raises an exception.
class Alarm(Exception):
    pass

def handler(signum, frame):
    raise Alarm

class ItimerTest(unittest.TestCase):

    def setUp(self):
        # Make sure the signal handler isn't left in from a previous test.
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

    def tearDown(self):
        # Make sure the signal handler is removed.
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

    def test_itimer_zero(self):
        # Set up the signal handler.
        signal.signal(signal.SIGALRM, handler)
        # Try setting the itimer for zero seconds.
        signal.setitimer(signal.ITIMER_REAL, 0)
        # Make sure the signal handler is called.
        self.assertRaises(Alarm, time.sleep, 0.1)
