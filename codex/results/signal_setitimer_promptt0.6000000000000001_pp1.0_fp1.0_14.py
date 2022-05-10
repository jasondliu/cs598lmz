import signal
# Test signal.setitimer() and signal.getitimer()

import os
import signal
import time
import unittest

from test.support import run_unittest, reap_threads


class TimerTests(unittest.TestCase):
    def setUp(self):
        self.called = False
        self.alarm_received = False
        self.child_alarm_received = False

    def alarm_handler(self, signum, frame):
        self.alarm_received = True

    def child_alarm_handler(self, signum, frame):
        self.child_alarm_received = True

    def test_itimer_virtual(self):
        self.called = False

        def handler(signum, frame):
            self.called = True

        signal.signal(signal.SIGVTALRM, handler)
        signal.setitimer(signal.ITIMER_VIRTUAL, 0.2)
        time.sleep(0.1)
        self.assertFalse(self.called)
        time.sleep(0.2)
        self
