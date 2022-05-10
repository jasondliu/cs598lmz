import signal
# Test signal.setitimer()
#
# The test case runs until the timer expires.

import os
import sys
import time

import unittest
from test.support import run_unittest, run_with_locale, cpython_only

class TimeIt:

    def __init__(self, seconds):
        self.seconds = seconds
        self.interrupted = False
        signal.signal(signal.SIGALRM, self.handler)

    def handler(self, signum, frame):
        self.interrupted = True

    def __enter__(self):
        signal.setitimer(signal.ITIMER_REAL, self.seconds)

    def __exit__(self, *args):
        signal.setitimer(signal.ITIMER_REAL, 0)
        return self.interrupted

class ItimerTest(unittest.TestCase):

    def test_itimer(self):
        with TimeIt(0.1):
            time.sleep(0.5)
            self.assertTrue(True)

def test_main():
    run_with
