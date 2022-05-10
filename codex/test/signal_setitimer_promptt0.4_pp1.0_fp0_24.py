import signal
# Test signal.setitimer()
#
# This test is Linux specific, it uses the SIGVTALRM signal.
#
# This test is skipped if the platform does not support setitimer().

import os
import sys
import time
import unittest
from test.support import run_unittest, cpython_only, import_module

signal = import_module('signal')

@cpython_only
class SetitimerTest(unittest.TestCase):
    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

    def alarm_handler(self, signum, frame):
        pass

    def test_setitimer(self):
        if not hasattr(signal, "setitimer"):
            self.skipTest("platform does not support setitimer()")
