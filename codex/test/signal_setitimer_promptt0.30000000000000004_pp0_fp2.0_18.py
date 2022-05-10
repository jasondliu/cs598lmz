import signal
# Test signal.setitimer()
#
# This is a test for setitimer() and getitimer()
#
# setitimer(which, seconds, interval=0)
#
# Set the timer which to fire after value seconds and
# after that every interval seconds.
#
# The timer can be one of:
# signal.ITIMER_REAL
# signal.ITIMER_VIRTUAL
# signal.ITIMER_PROF
#
# If interval is 0, then the timer will only fire once.
#
# The return value is an (itimer_value, itimer_interval) tuple.
#
# See the man page for setitimer(2) for more information.
#
# The timer can be cleared by setting seconds to 0.
#
# The timer can be read by calling getitimer()

import os
import signal
import sys
import time

# This is a little helper function to print the timer
def printTimer(prefix, itimer):
    if itimer[0] == 0 and itimer[1] == 0:
        print(prefix + ": None")
