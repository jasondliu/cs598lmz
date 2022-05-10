import signal
# Test signal.setitimer()
#
# This test sets the SIGALRM signal handler to a function that increments a
# global variable and sets the alarm to go off in 0.5 seconds.
# The test then enters a tight loop that takes 1 second to execute, and
# checks that the variable was incremented at least twice, which means that
# the alarm went off at least twice.
#

import unittest
from test.support import run_unittest, import_module

signal = import_module('signal')

# This test is unreliable on all platforms, but especially so on Windows,
# where the resolution of the system clock is only 15ms.
@unittest.skip("test is unreliable")
class SetitimerTestCase(unittest.TestCase):
    def setUp(self):
        self.alarm_received = 0
        self.old_alarm_handler = signal.signal(signal.SIGALRM, self.alarm_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm_handler)

   
