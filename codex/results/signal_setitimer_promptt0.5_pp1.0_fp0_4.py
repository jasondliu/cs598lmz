import signal
# Test signal.setitimer() with SIGALRM.
#
# This is a regression test for http://bugs.python.org/issue24313.

import os
import sys
import time
import unittest
from test.support import run_unittest

if sys.platform == 'win32':
    import msvcrt
    msvcrt.SetConsoleCtrlHandler(lambda x: True, True)


class TestSetitimer(unittest.TestCase):
    def test_alarm(self):
        # Issue #24313: Test that signal.setitimer(signal.ITIMER_REAL, ...)
        # works properly.
        def handler(signum, frame):
            pass
        signal.signal(signal.SIGALRM, handler)
        signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)
        time.sleep(0.5)
        signal.setitimer(signal.ITIMER_REAL, 0.0, 0.0)
        time.sleep(1.0)
        signal.
