import signal
# Test signal.setitimer()
#
# (c) Mit authors 1994-2020
#
# The package is distributed under the MIT/X11 License.
#
# THIS PROGRAM IS PROVIDED AS IS, WITH NO WARRANTY. USE IS AT THE USER’S
# RISK.

import os
import sys
import time

from mit.globals import *
from mit.test import TestCase


class ItimerTest(TestCase):

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)
        self.old_itimer = signal.setitimer(signal.ITIMER_REAL, 0)
        self.alarm_fired = False
        self.alarm_count = 0

    def tearDown(self):
        signal.setitimer(signal.ITIMER_REAL, self.old_itimer)
        signal.signal(signal.SIGALRM, self.old_alarm)

    def alarm_handler(self, *args):
        self.alarm
