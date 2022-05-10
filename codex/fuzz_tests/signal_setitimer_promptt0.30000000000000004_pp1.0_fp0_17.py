import signal
# Test signal.setitimer()

import os
import signal
import time

def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)

# This should cause the handler to be called every 2 seconds.
signal.setitimer(signal.ITIMER_REAL, 2, 2)

for i in range(5):
    print 'Sleeping', i
    time.sleep(1)

signal.setitimer(signal.ITIMER_REAL, 0)
print 'Done'
