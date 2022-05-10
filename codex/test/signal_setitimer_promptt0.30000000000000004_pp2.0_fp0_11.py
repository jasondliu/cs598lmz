import signal
# Test signal.setitimer
#
# This test is a bit tricky, because we have to set up a signal handler
# that will be called in the middle of the test.  If the signal handler
# is called too early, the test will fail.  If the signal handler is
# called too late, the test will hang.

import sys
import time

# This is a signal handler.  It sets the global variable 'called' to
# True.  It also sets the global variable 'interval' to the value of
# the interval timer.
def handler(signum, frame):
    global called
    global interval
    called = True
    interval = signal.getitimer(signal.ITIMER_REAL)

# This is the main test function.  It sets up a signal handler, and
# then sets the interval timer.  It then waits for the signal handler
# to be called.  If the signal handler is called too early, the test
# fails.  If the signal handler is called too late, the test hangs.
def test():
    global called
    global interval
    called = False
    interval = 0
    signal
