import signal
# Test signal.setitimer()

import sys
import os
import time

def handler(signum, frame):
    print('Got signal', signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Wait for the timer to expire 10 times.
for i in range(1, 10):
    print('Sleeping', i)
    time.sleep(1)

# Set the timer to 0.0, 0.0 to cancel it.
signal.setitimer(signal.ITIMER_REAL, 0.0, 0.0)

# Wait for the timer to expire 10 times.
for i in range(1, 10):
    print('Sleeping', i)
    time.sleep(1)
