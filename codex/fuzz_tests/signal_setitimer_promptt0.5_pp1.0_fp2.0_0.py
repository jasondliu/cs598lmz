import signal
# Test signal.setitimer() and signal.getitimer().
#
# This test is Linux-specific, because it relies on the kernel's
# ITIMER_PROF timer.

import os
import sys
import time
import unittest

from test import support

if sys.platform == 'win32':
    raise unittest.SkipTest("SIGALRM not supported on Windows")

# The test fails if the interval is too large, so we use a small value.
TEST_INTERVAL = 0.1

class TestSetitimer(unittest.TestCase):
    def setUp(self):
        self.sigprof_reached = False

    def sigprof(self, signum, frame):
        self.sigprof_reached = True

    def test_setitimer(self):
        signal.signal(signal.SIGPROF, self.sigprof)
        signal.setitimer(signal.ITIMER_PROF, TEST_INTERVAL, 0)
        time.sleep(2*TEST_INTERVAL)
        self.assertTrue(self
