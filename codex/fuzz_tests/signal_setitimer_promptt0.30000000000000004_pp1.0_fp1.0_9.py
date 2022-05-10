import signal
# Test signal.setitimer()

import os
import sys
import time
import signal

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# Install the signal handler and set a 1-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)
