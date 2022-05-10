import signal
# Test signal.setitimer() with SIGALRM
import sys
import time
import unittest
from test import support

try:
    signal.setitimer(signal.ITIMER_REAL, 0)
except (AttributeError, ValueError):
    raise unittest.SkipTest("need setitimer()")

itimer_virtual = getattr(signal, 'ITIMER_VIRTUAL', None)
itimer_prof = getattr(signal, 'ITIMER_PROF', None)

def handler(signum, frame):
    print('handler', signum, frame)
    raise SystemExit

class ItimerTest(unittest.TestCase):
    def setUp(self):
        self.oldalrm = signal.signal(signal.SIGALRM, handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.oldalrm)

    def test_itimer_zero(self):
        self.assertRaises(ValueError, signal.setitimer, signal.ITIMER_REAL, -1
