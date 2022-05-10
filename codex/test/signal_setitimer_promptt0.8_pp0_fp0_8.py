import signal
# Test signal.setitimer() with SIGPROF.
#
# Based on Lib/test/test_signal.py.
#
# This test should be skipped on macOS (and other platforms)
# where SIGPROF is not supported.
#
# Skip this test if the timer resolution is too low.

import os
import sys
import time
import unittest
import signal
import subprocess
from test import support


class SigprofTestCase(unittest.TestCase):

    def setUp(self):
        self._savealarm = signal.setitimer(signal.ITIMER_REAL, 0, 0)
        self._saveprof = signal.setitimer(signal.ITIMER_PROF, 0, 0)

    def tearDown(self):
        signal.setitimer(signal.ITIMER_REAL, *self._savealarm)
        signal.setitimer(signal.ITIMER_PROF, *self._saveprof)

    def timer_resolution_check(self):
        test_interval = 0.01
        precision_needed = 0.005
