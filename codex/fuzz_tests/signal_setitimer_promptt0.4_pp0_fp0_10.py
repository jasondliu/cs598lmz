import signal
# Test signal.setitimer()
#
# The test is supposed to be run in a separate process, so that
# the signal handler is not interrupted by the timer.
#
# The test is supposed to be run in a separate process, so that
# the signal handler is not interrupted by the timer.
#
# This test is Linux specific.
#
import sys
import time

from test.support import verbose, TestFailed, TestSkipped

#
# Test signal.setitimer()
#

#
# Test signal.setitimer()
#

def alarm_handler(signum, frame):
    if verbose:
        print("alarm_handler: signum", signum)

def test_setitimer():
    #
    # First, test that the signal handler is called as expected.
    #

    # Set up the signal handler
    signal.signal(signal.SIGALRM, alarm_handler)

    # Set the timer
    signal.setitimer(signal.ITIMER_REAL, 2, 0)

    # Sleep for a while
    time.sleep(1
