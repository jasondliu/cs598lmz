import signal
# Test signal.setitimer() and signal.getitimer()

import os
import sys
import time
import signal

import unittest
from test.support import run_unittest, verbose, TESTFN, unlink

if sys.platform[:3] == 'win':
    verbose = 0

if sys.platform[:3] == 'win':
    timer = signal.ITIMER_REAL
    delay = 0.02
    error = 0.02
    TIMER_MAX = 214747
else:
    timer = signal.ITIMER_VIRTUAL
    delay = 0.02
    error = 0.02
    TIMER_MAX = 214748

def alarm_received(n, stack):
    global alarm_counter
    alarm_counter = alarm_counter + 1

alarm_counter = 0

class AlarmTest(unittest.TestCase):
    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, alarm_received)

    def tearDown(self):
        signal.signal(
