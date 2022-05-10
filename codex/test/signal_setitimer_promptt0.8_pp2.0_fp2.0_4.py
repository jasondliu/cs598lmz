import signal
# Test signal.setitimer and signal.itimer functions
# Uses SIGALRM, so runs on Unix only.

import sys, time
import unittest

from test import support

sig_count = 0


def handler(signum, frame):
    global sig_count
    sig_count += 1
    raise OSError

class ItimerTest(unittest.TestCase):
    # Can't use unittest.skip on old Pythons, because it works by
    # raising RuntimeError, which gets swallowed by the signal handler
    def test_itimer_basic(self):
        try:
            signal.setitimer(signal.ITIMER_REAL, 0.1)
        except ValueError:
            raise unittest.SkipTest("itimer not supported")

    def test_itimer_zero(self):
        signal.signal(signal.SIGALRM, handler)
        signal.setitimer(signal.ITIMER_REAL, 0.1)
