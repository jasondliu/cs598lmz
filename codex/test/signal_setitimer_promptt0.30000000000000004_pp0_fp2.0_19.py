import signal
# Test signal.setitimer()
#
# This is a test for the setitimer() function found in the signal module.
# It tests the basic functionality of the function.

import os
import signal
import sys
import time
import unittest

from test.support import run_unittest, reap_children, get_attribute

#
# Constants
#

# The number of seconds to sleep when testing the timer.
SLEEP_TIME = 0.1

# The number of seconds to wait for the timer to expire.
WAIT_TIME = 1.0

#
# Code
#

class SetitimerTest(unittest.TestCase):
    # Test setitimer()

    def setUp(self):
        self.pid = os.getpid()
        self.signalled = False

    def tearDown(self):
        if self.signalled:
            self.signalled = False
            signal.signal(signal.SIGALRM, signal.SIG_DFL)

    def alarm_handler(self, signum, frame):
        self.signalled = True


