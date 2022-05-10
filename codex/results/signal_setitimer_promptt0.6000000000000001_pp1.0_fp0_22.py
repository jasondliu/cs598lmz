import signal
# Test signal.setitimer() with SIGPROF and SIGALRM
#
# Note, the test is not very good, as it doesn't check that SIGPROF is
# actually generated.

import sys
import time

#
# Check that SIGPROF and SIGALRM work
#

def handler(signum, frame):
    print "Handler called with signal %d" % signum

signal.signal(signal.SIGPROF, handler)
signal.signal(signal.SIGALRM, handler)

# set the interval timer to fire after 1 second
signal.setitimer(signal.ITIMER_PROF, 1, 1)
# set the alarm clock to fire after 2 seconds
signal.alarm(2)
# sleep for 3 seconds
time.sleep(3)
