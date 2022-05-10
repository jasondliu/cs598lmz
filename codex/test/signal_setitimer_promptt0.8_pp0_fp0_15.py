import signal
# Test signal.setitimer(), which can be used for profiling.

import os
import sys

#if sys.platform.startswith('linux'):
#    timer = signal.ITIMER_PROF
#elif sys.platform.startswith('bsd'):
#    timer = signal.ITIMER_REAL
#else:
#    # Unsupported platform.
#    sys.exit(0)

# A handler that counts how often it is called.
COUNTER = [0]
def handler(signum, frame):
    COUNTER[0] += 1

# Register the handler.
signal.signal(signal.SIGPROF, handler)

# Start the timer.
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

# Wait sufficient time for the timer to be called a few times.
for i in range(5):
    x = i ** 2

# Stop the timer.
signal.setitimer(signal.ITIMER_PROF, 0, 0)

# Check that handler was
