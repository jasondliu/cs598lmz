import signal
# Test signal.setitimer with alarm

import os, signal, sys

def handler(signum, frame):
    print 'handler called for signal', signum
    if signum == signal.SIGALRM:
        raise Exception, 'SIGALRM received'

signal.signal(signal.SIGALRM, handler)

# Wait for 2 seconds
signal.setitimer(signal.ITIMER_REAL, 2)

# Wait for 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# Wait for 3 seconds
signal.setitimer(signal.ITIMER_REAL, 3)

# Wait for 2 seconds
signal.setitimer(signal.ITIMER_REAL, 2)

# Wait for 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# Wait for 3 seconds
signal.setitimer(signal.ITIMER_REAL, 3)

# Wait for 2 seconds
signal.setitimer(signal.ITIM
