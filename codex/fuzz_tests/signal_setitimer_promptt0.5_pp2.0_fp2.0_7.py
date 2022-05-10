import signal
# Test signal.setitimer()
import unittest
from test import support

class SetitimerTest(unittest.TestCase):

    def setUp(self):
        self.called = False
        self.scheduled = False
        self.alarm_received = False
        self.scheduled_count = 0
        self.alarm_count = 0
        self.signal_count = 0
        self.signal_received = False
        self.interrupted = False

    def alarm_handler(self, signum, frame):
        self.alarm_received = True
        self.alarm_count += 1

    def signal_handler(self, signum, frame):
        self.signal_received = True
        self.signal_count += 1

    def scheduled_handler(self):
        self.scheduled = True
        self.scheduled_count += 1

    def test_itimer_virtual(self):
        # Issue #5976: itimer signal handler should get called even if the
        # thread executing the signal handler gets interrupted by another
        # thread.
        #

