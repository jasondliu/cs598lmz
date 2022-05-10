import signal
# Test signal.setitimer() and signal.getitimer()
#
# Check that the timer is really expired by calling setitimer()
# with the same value and checking that no signal is received.

import sys
import time

from test.support import run_unittest, wait_process

import unittest

from test.support import get_attribute

#
# The unittest infrastructure seems to install a SIGALRM handler which
# prevents us from using this signal, so we pick another one
#

TEST_SIGNAL = signal.SIGUSR1

class SIGALRMTest(unittest.TestCase):
    def setUp(self):
        self.old_handler = signal.signal(TEST_SIGNAL, self.handler)
        self.alarm_fired = False
        self.old_interval = signal.setitimer(signal.ITIMER_REAL, 0.1)
        self.assertEqual(self.old_interval, 0.0)

