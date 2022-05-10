import signal
# Test signal.setitimer

import signal
import time

def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)

# This should only be needed on a Unix system that supports SIGALRM
# signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
# time.sleep(5)

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
time.sleep(5)

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
time.sleep(5)

print 'Main program'
