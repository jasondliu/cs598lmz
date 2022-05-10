import signal
# Test signal.setitimer()

import sys
import time

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Kaboom")

signal.signal(signal.SIGALRM, handler)

# Register a signal handler for SIGALRM
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# This will also cause the alarm signal to be raised
time.sleep(0.2)

print 'Exiting normally'
