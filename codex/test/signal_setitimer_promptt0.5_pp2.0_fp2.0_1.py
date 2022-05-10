import signal
# Test signal.setitimer() and signal.getitimer()

import signal
import sys

def handler(signum, frame):
    print('Signal handler called with signal', signum)

signal.signal(signal.SIGALRM, handler)

# Start a timer that will go off in 2 seconds
signal.setitimer(signal.ITIMER_REAL, 0, 2)

print('About to sleep')
sys.stdout.flush()

# This will block until the timer goes off
signal.pause()

print('Done')

# The timer went off and the signal handler was called
# Now get the timer remaining time
remaining = signal.getitimer(signal.ITIMER_REAL)

print('Remaining:', remaining)

# The timer is still running, so the remaining time is less than 2 seconds
