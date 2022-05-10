import signal
# Test signal.setitimer()

import os
import time
import unittest
from test import support

class TestSetitimer(unittest.TestCase):
    def setUp(self):
        self.sig_handler_called = 0
        self.sig_handler_pid = 0
        self.sig_handler_signum = 0
        self.sig_handler_time = 0
        self.sig_handler_itimer = 0
        self.sig_handler_itimer_interval = 0.0

    def sig_handler(self, signum, frame):
        self.sig_handler_called += 1
        self.sig_handler_pid = os.getpid()
        self.sig_handler_signum = signum
        self.sig_handler_time = time.time()
        self.sig_handler_itimer = signal.getitimer(signal.ITIMER_REAL)
        self.sig_handler_itimer_interval = self.sig_handler_itimer[0]

