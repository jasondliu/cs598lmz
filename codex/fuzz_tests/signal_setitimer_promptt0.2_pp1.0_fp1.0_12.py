import signal
# Test signal.setitimer()
#
# This test is not very good, because it doesn't check that the timer
# actually works.  It just checks that the function doesn't crash.
#
# This test is not run by default, because it takes a long time to run.
# To run it, do:
#
#    python test_signal.py -u network
#

import signal
import time

def handler(signum, frame):
    pass

signal.signal(signal.SIGALRM, handler)

# Set the timer to go off in 1 second.
signal.setitimer(signal.ITIMER_REAL, 1, 0)

# Wait for the timer to go off.
time.sleep(2)

# Set the timer to go off in 1 second.
signal.setitimer(signal.ITIMER_REAL, 1, 0)

# Wait for the timer to go off.
time.sleep(2)

# Set the timer to go off in 1 second.
signal.setitimer(signal.ITIMER_REAL
