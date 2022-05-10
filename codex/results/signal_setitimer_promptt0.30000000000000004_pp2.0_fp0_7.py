import signal
# Test signal.setitimer()
#
# This test case is for the setitimer() function found in the signal
# module.  The function is passed a signal number, and a tuple of
# integers representing the interval and the value to set the timer
# to.  The function returns the old value of the timer.  The timer
# will generate a SIGALRM signal when it expires.
#
# The test case will set the timer to a known value, then check that
# the timer is set to that value.  The test case will then sleep for
# a short period, and check that the timer has expired.  The test
# case will then set the timer to a new value, and check that the
# timer is set to that value.  The test case will then sleep for a
# short period, and check that the timer has expired.  The test case
# will then set the timer to 0, and check that the timer has
# expired.

import os
import signal
import time
import unittest

from test.support import run_unittest, get_attribute

# The signal module is not available on all platforms
signal = get_
