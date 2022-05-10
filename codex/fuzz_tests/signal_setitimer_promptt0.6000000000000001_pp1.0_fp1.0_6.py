import signal
# Test signal.setitimer() and signal.getitimer().
# This is only supported on Unix.

import unittest
from test.support import import_module
signal = import_module('signal')

class AlarmTest(unittest.TestCase):

    def setUp(self):
        self.sig_handler_args = []
        self.sig_handler_called = 0
        self.old_handler = signal.signal(signal.SIGALRM,
                                         self.catch_alarm)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_handler)

    def catch_alarm(self, *args):
        self.sig_handler_args.append(args)
        self.sig_handler_called += 1

    def test_setitimer(self):
        self.assertRaises(ValueError, signal.setitimer, -1, 1)
        self.assertRaises(ValueError, signal.setitimer, signal.ITIMER_REAL,
                          -1)
       
