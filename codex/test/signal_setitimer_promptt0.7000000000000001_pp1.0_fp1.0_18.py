import signal
# Test signal.setitimer
# See also the test in test_itimer_virtual.py

import unittest
from test import support

from signal import SIGALRM, ITIMER_REAL

from time import sleep, time
from socket import socket

def alarm_received(n, stack):
    pass

class ItimerTest(unittest.TestCase):
    def setUp(self):
        signal.signal(SIGALRM, alarm_received)

    def tearDown(self):
        self.setitimer(0, 0)
        signal.signal(SIGALRM, signal.SIG_DFL)

    def setitimer(self, *args):
        if hasattr(signal, 'setitimer'):
            signal.setitimer(*args)
        else:
            signal.setitimer_add(*args)

