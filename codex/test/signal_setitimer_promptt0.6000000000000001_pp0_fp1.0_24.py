import signal
# Test signal.setitimer
#
# Note: We only test the non-blocking case.

import unittest
import os
import sys
import time

from test.support import run_unittest, reap_threads


class TestSetitimer(unittest.TestCase):
    def setUp(self):
        self.sig_received = 0
        self.old_handler = signal.signal(signal.SIGALRM, self.handler)

    def tearDown(self):
        # Reset the alarm
        signal.setitimer(signal.ITIMER_REAL, 0, 0)
        # Restore the old handler
        signal.signal(signal.SIGALRM, self.old_handler)

    def handler(self, signum, frame):
        self.sig_received += 1
        raise SystemExit

    def test_basic(self):
        self.assertEqual(signal.setitimer(signal.ITIMER_REAL, 1, 0), (0, 0))
        time.sleep(2)
