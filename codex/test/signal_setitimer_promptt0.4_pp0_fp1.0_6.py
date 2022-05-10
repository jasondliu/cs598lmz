import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)
#
# ITIMER_VIRTUAL is not supported on Mac OS X
#
# ITIMER_VIRTUAL decrements in units of the time spent executing user
# instructions.  This timer is slower than ITIMER_REAL, but it does not
# decrement when the system is executing system calls on behalf of the
# process, when the process is blocked in user space, or when the process is
# running in kernel space.  This timer may also be used by the process as a
# private alarm clock.
#
# The value of this timer is returned by the getrusage() system call.

import os
import signal
import sys
import time

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
