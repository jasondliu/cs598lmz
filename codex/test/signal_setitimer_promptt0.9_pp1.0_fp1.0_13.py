import signal
# Test signal.setitimer() for sending a signal every few seconds.

import os
import unittest

from test import support
from test.support import import_module

# Skip test if setitimer(2) is not available.
setitimer = import_module('select').setitimer

timeslicesleep = 0.1

def timeslice_handler(signal, frame):
    print(".", end="")
    signal.alarm(int(timeslicesleep))

class AlarmTester(unittest.TestCase):

    def tearDown(self):
        signal.alarm(0)

    def test_alarm(self):
        # Signal delivery is quite unreliable, so we expect to
        # receive between 8 and 12 SIGALRM signals, with the total
        # time being between 80% and 120% of the expected time.
        sleeptime = timeslicesleep * 10
        signal.signal(signal.SIGALRM, timeslice_handler)
        signal.alarm(int(timeslicesleep))
        print()
        os.stat('/')
