import signal
# Test signal.setitimer()
#
# This test is not very good, because it relies on the timer
# expiring while the test is running.  If the test is run on a
# heavily loaded machine, the timer may not expire in time.
#
# Written by Bill Tutt.  Modified for Python by Guido van Rossum.

import time
import sys

def handler(signum, frame):
    print 'handler'
    sys.exit(0)

signal.signal(signal.SIGALRM, handler)

# Set an alarm for 1 second in the future
signal.setitimer(signal.ITIMER_REAL, 1)

# Busy loop
while 1:
    pass
