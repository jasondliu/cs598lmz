import signal
# Test signal.setitimer() on Mac OS X
# See http://bugs.python.org/issue20800

import os
import time
import unittest

from test import support

class ItimerTest(unittest.TestCase):
    def setUp(self):
        self.pid = os.getpid()
        self.times = []
        self.alarm_raised = False

    def callback(self, signum, frame):
        self.alarm_raised = True
        self.times.append(time.time())
        if len(self.times) > 1:
            self.assertGreater(self.times[-1], self.times[-2])

    def test_itimer_basic(self):
        # Test basic functionality
        signal.signal(signal.SIGALRM, self.callback)
        signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
        time.sleep(0.25)
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

        self.assertGreat
