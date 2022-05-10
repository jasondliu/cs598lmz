import signal
# Test signal.setitimer
#
# This tests setting the ITIMER_PROF timer.  The timer is set for 1 second
# and we sleep for 1.5 seconds.  We expect to receive a SIGPROF signal.
#
# Python signal module sends SIGVTALRM on Linux instead of SIGPROF.  If
# Python is compiled with ucontext, then it sends the correct signal.
#
# Python signal module sends SIGALRM on OSX instead of SIGPROF.

import os, sys
import signal
import time

def handler(signum, frame):
    print "handler called with signal", signum

signal.signal(signal.SIGPROF, handler)
signal.setitimer(signal.ITIMER_PROF, 1, 0)

# If we're running with ucontext, then the signal handler will be called.
# Otherwise, the signal handler won't be called.
time.sleep(1.5)

print "done"
