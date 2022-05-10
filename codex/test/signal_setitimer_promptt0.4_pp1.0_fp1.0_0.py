import signal
# Test signal.setitimer()
#
# This test is not complete, it only tests the basic functionality of
# setitimer().  It does not test the actual timing.

import os, sys, time
import unittest
from test import support

class SetitimerTest(unittest.TestCase):
    def setUp(self):
        self.sigalrm_caught = 0
        self.oldalarm = signal.signal(signal.SIGALRM, self.sigalrm_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.oldalarm)

    def sigalrm_handler(self, signum, frame):
        self.sigalrm_caught += 1

    def test_setitimer(self):
        signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
        time.sleep(0.2)
        self.assertTrue(self.sigalrm_caught > 0)
