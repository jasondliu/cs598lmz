import signal
# Test signal.setitimer with timer_type == ITIMER_VIRTUAL and
# interval > value.  This test will either run exactly interval
# seconds or sys.maxint seconds, whichever is less.
import sys
import time
import unittest


class Handler:
    def __init__(self):
        self.caught = 0

    def __call__(self, signum, frame):
        self.caught += 1


class TestItimerVirtual(unittest.TestCase):

    def setUp(self):
        self.interval = 2
        self.handler = Handler()
        signal.signal(signal.SIGVTALRM, self.handler)
        signal.setitimer(signal.ITIMER_VIRTUAL, self.interval, self.interval)

    def tearDown(self):
        signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)

    def test_itimer_virtual(self):
        # Run SELF.INTERVAL seconds, or at least 1 tick.
        end_time = time.time() + min
