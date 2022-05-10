import signal
# Test signal.setitimer() and support code,
# including the alarm() system call which is the C library's
# setitimer() wrapper.

import os
import time
import sys
import unittest

def _is_alarm_supported():
    # Travis CI does not have setitimer()/getitimer() functions. Therefore
    # disable this test case.
    if 'TRAVIS' in os.environ:
        print('Skip test case because setitimer() is not supported under travis.')
        return False
    return True


def handler(signum, frame):
    pass

# get the current real time and cpu time
def get_times():
    return time.time(), time.clock()

class BaseAlarmTest(unittest.TestCase):
    def setUp(self):
        if not _is_alarm_supported():
            self.skipTest('setitimer() is not supported under travis - skip test')

    def tearDown(self):
        signal.setitimer(signal.ITIMER_REAL, 0)

