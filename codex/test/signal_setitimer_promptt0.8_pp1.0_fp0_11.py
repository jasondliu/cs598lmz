import signal
# Test signal.setitimer() and the SIGALRM and SIGVTALRM signals.
import unittest
import os
import sys
import time
import subprocess
import errno
import pickle
import test.support
import contextlib


class TestAlarm(unittest.TestCase):
    def setUp(self):
        self.oldalarm = signal.signal(signal.SIGALRM, signal.default_int_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.oldalarm)

    def alarm(self, secs):
        signal.setitimer(signal.ITIMER_REAL, secs)
        try:
            signal.pause()
        except RuntimeError:
            pass
        self.assertEqual(signal.setitimer(signal.ITIMER_REAL, 0), (0.0, 0.0))

    def test_alarm(self):
        self.assertEqual(signal.alarm(1), 0)
