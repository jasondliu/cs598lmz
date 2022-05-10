import signal
# Test signal.setitimer()
import sys

import unittest
from test import support
from test.support import get_attribute

from socket import socketpair
import _signal
from _signal import SIGALRM, ITIMER_REAL, ITIMER_VIRTUAL, ITIMER_PROF

# Skip tests if setitimer isn't available
requires_setitimer = unittest.skipUnless(hasattr(_signal, "setitimer"),
                                         "requires setitimer()")

class SigAlarm(Exception):
    pass

def alarm_handler(*args):
    raise SigAlarm

class SignalSetitimerTest(unittest.TestCase):

    def setUp(self):
        self.oldalarm = signal.signal(SIGALRM, alarm_handler)
        self.olditimer = signal.setitimer(ITIMER_REAL, 0, 0)

    def tearDown(self):
        signal.signal(SIGALRM, self.oldalarm)
