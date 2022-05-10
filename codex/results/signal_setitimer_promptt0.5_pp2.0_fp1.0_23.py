import signal
# Test signal.setitimer() and signal.getitimer()

# The values of the timer are not very precise.
# On a 2GHz P4, the timer usually expires 50-100ms early.
# On a 266MHz Sparc, the timer usually expires about 2s early.

import sys
import time

def handler(signum, frame):
    print 'handler'
    sys.exit(0)

signal.signal(signal.SIGALRM, handler)

# First set an alarm
signal.setitimer(signal.ITIMER_REAL, 0.2, 0)
print 'Sleeping for 1 second'
time.sleep(1.0)
print 'Done sleeping'

# Now check the time left
left = signal.getitimer(signal.ITIMER_REAL)
print 'Time left:', left
if left[0] > 0.18:
    print 'error: got', left[0], 'seconds left'

# Now set a new alarm
signal.setitimer(signal.ITIMER_REAL, 0.2, 0
