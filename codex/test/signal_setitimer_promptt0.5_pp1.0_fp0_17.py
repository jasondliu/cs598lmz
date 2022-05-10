import signal
# Test signal.setitimer
# This test is Linux specific.

import os, sys
if sys.platform[:3] != 'win':
    print('skipped: setitimer not available on this platform')
    sys.exit()


import unittest
from test.support import run_unittest, import_module

import time

class Handler:
    def __init__(self):
        self.called = 0
        self.alarm_received = 0
        self.child_alarm_received = 0

    def __call__(self, signum, frame):
        self.called += 1
        if signum == signal.SIGALRM:
            self.alarm_received += 1
        elif signum == signal.SIGCHLD:
            self.child_alarm_received += 1
        else:
            raise ValueError("Unexpected signal")

class ItimerTest(unittest.TestCase):
    def test_setitimer(self):
        h = Handler()
        signal.signal(signal.SIGALRM, h)
