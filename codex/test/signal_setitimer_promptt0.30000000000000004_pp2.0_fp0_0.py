import signal
# Test signal.setitimer()
#
# This is a test for http://bugs.python.org/issue1798391
#
# This test is expected to fail on platforms that do not support
# setitimer(), including Windows.

import os
import unittest

from test import support

# Skip this test if setitimer() is not available.
if not hasattr(signal, 'setitimer'):
    raise unittest.SkipTest("platform does not support setitimer()")

# Skip this test if SIGALRM is not available.
if not hasattr(signal, 'SIGALRM'):
    raise unittest.SkipTest("platform does not support SIGALRM")

class AlarmTest(unittest.TestCase):
    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

