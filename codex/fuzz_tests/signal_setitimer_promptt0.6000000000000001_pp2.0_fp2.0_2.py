import signal
# Test signal.setitimer.
#
# This test is only supported on systems that support itimer, and
# only when the test is run over ssh, because the test hangs when
# run directly on the console.

# This test hangs on Windows.

import unittest
from test.support import run_unittest, import_module
from test.support import time_out, TESTFN, HOST, verbose

# Skip test if there is no itimer support.
itimer = import_module('signal')
if not hasattr(itimer, 'setitimer'):
    raise unittest.SkipTest("platform has no itimer support")

# Skip test if run over the console
if not HOST:
    raise unittest.SkipTest("test hangs on the console")

verbose = 0

class ItimerTest(unittest.TestCase):
    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)
        self.old_itimer = itimer.getitimer(itimer.ITIM
