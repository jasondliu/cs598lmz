import signal
# Test signal.setitimer

# setitimer is only supported on Linux and Mac OS X
# and only for Python built with thread support.
if not hasattr(signal, 'setitimer'):
    print('setitimer is not supported')
    raise SystemExit
if not hasattr(signal, 'ITIMER_REAL'):
    print('ITIMER_REAL is not supported')
    raise SystemExit

import sys
import time
import unittest

from test.support import run_unittest, TestFailed, verbose

class TestSetitimer(unittest.TestCase):
    def setUp(self):
        self.caught = 0
        signal.signal(signal.SIGALRM, self.handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, signal.SIG_DFL)
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

    def handler(self, sig, frame):
        self.caught += 1

