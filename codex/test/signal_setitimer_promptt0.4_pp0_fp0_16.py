import signal
# Test signal.setitimer
#
# This testcase is part of the following thread:
# http://mail.python.org/pipermail/python-dev/2003-August/038131.html
#
# Contributed by Thomas Heller.

import unittest
import time

from test.support import run_unittest, get_attribute

class TestSetitimer(unittest.TestCase):

    def setUp(self):
        self.oldalarm = signal.signal(signal.SIGALRM, self.alarm_handler)
        signal.setitimer(signal.ITIMER_REAL, 1, 0)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.oldalarm)
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

    def alarm_handler(self, signum, frame):
        self.alarm_fired = True

    def test_alarm(self):
        self.alarm_fired = False
        time.sleep(2)
