import signal
# Test signal.setitimer()

# This test exercises the implementation of setitimer().
#
# It ensures that the timer is not set if the first parameter is 0
# (timer disabled)
#
# It also checks that the timer is armed as expected, when passing
# non-zero values as the first parameter.
#
# Additionally, it ensures that the timer is armed as expected when
# using the ITIMER_REAL and ITIMER_VIRTUAL constants.

import os
import sys
import time
import signal
import unittest

# Used in the test.
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1

# Timeout for the test.
TIMEOUT = 10

# Time to sleep for the test.
SLEEP_TIME = 0.5

# How much does the timer can differ from the expected value.
# (This is for the real timer).
TIMER_TOLERANCE = 0.01

class Alarm(Exception):
    pass

class AlarmHandler:
    def __init__(self):
        self.catched = False

   
