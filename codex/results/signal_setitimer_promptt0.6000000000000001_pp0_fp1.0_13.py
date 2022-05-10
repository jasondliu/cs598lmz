import signal
# Test signal.setitimer()

import os
import signal
import time

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Tell the signal module to notice the signal (Python installs a handler that
# ignores the signal by default)
signal.signal(signal.SIGALRM, handler)

# Start a timer.  We'll get SIGALRM when the timer is up
signal.setitimer(signal.ITIMER_REAL, 2)

print 'Calling time.sleep()'
time.sleep(10)

print 'Exiting normally'
