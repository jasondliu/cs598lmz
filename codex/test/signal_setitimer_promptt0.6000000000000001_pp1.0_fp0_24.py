import signal
# Test signal.setitimer() and signal.getitimer().

import os
import sys
import unittest
from test.support import run_unittest, get_attribute

signal = __import__('signal')

# These are new in Python 2.7.
has_itimer = hasattr(signal, "setitimer") and hasattr(signal, "getitimer")

@unittest.skipUnless(has_itimer, "test needs signal.setitimer() and signal.getitimer()")
class ItimerTest(unittest.TestCase):

    def setUp(self):
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

    def test_getitimer(self):
        signal.setitimer(signal.ITIMER_REAL, 0.1)
        self.assertEqual(signal.getitimer(signal.ITIMER_REAL), 0.1)
        signal.setitimer(signal.ITIMER_REAL, 0)
