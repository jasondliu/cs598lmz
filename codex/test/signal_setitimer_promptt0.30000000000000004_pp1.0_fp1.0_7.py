import signal
# Test signal.setitimer()
#
# This test is derived from the test_signal.py test from the Python
# standard library.

import unittest
from test.support import run_unittest, import_module

signal = import_module('signal')

class ItimerTest(unittest.TestCase):
    def setUp(self):
        self.oldalarm = signal.signal(signal.SIGALRM, self.alarm_handler)
        self.olditimer = signal.setitimer(signal.ITIMER_REAL, 0, 0)
        self.alarm_fired = False

    def tearDown(self):
        signal.setitimer(signal.ITIMER_REAL, *self.olditimer)
        signal.signal(signal.SIGALRM, self.oldalarm)

    def alarm_handler(self, signum, frame):
        self.alarm_fired = True

