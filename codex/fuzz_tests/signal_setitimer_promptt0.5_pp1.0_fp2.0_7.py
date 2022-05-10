import signal
# Test signal.setitimer()
#
# This test case is derived from Lib/test/test_signal.py.
# It is modified to use setitimer() instead of alarm()
#
# The original version is written by Greg Ward <gward@python.net>
# and is placed in the Public Domain.

import os
import unittest
import time

from test import support

try:
    signal.setitimer
except AttributeError:
    raise unittest.SkipTest("requires setitimer()")

signal.signal(signal.SIGALRM, lambda *args: None)

class ItimerTest(unittest.TestCase):
    def setUp(self):
        self.old_alarm = signal.setitimer(signal.ITIMER_REAL, 0)

    def tearDown(self):
        self.assertEqual(signal.setitimer(signal.ITIMER_REAL, 0), self.old_alarm)

    def pause_for_signal(self, seconds):
        # Sleep for a while, and check that
