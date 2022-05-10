import signal
# Test signal.setitimer
#
# This test is not run by default.  It will hang if the system doesn't
# support setitimer.  To run this test, execute this file directly.
#
# This test is not run by default because it hangs if the system doesn't
# support setitimer.

import os
import signal
import sys
import time
import unittest

from test import support

# This test is not run by default because it hangs if the system doesn't
# support setitimer.

class SetitimerTest(unittest.TestCase):

    def setUp(self):
        self.sigalrm_caught = 0
        self.old_alarm = signal.signal(signal.SIGALRM, self.sigalrm_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

    def sigalrm_handler(self, signum, frame):
        self.sigalrm_caught += 1

