import signal
# Test signal.setitimer()
#
# $Id: test_signal_itimer.py,v 1.1 2007/09/10 22:48:23 jriehl Exp $

import os
import sys
sys.path[0:0] = ['../..']
import unittest
from test import test_support

class ItimerTests(unittest.TestCase):

    def setUp(self):
        self.catcher = []
        self.old_alarm = signal.signal(signal.SIGALRM, self.catcher.append)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

    def test_itimer_basic(self):
        # Test setting an alarm
        signal.setitimer(signal.ITIMER_REAL, 0.2)
        time.sleep(0.1)
        self.assertEqual(len(self.catcher), 0)
        time.sleep(0.2)
        self.assertEqual(len(self.catcher), 1)

