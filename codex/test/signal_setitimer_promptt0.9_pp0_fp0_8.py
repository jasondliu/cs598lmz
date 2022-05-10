import signal
# Test signal.setitimer().

import signal, os

itimer_interval = 0.1 # seconds

caught = 0

def handler(*args):
    global caught
    caught = caught + 1

# Set up the signal handler.
signal.signal(signal.SIGALRM, handler)

# Set the itimer.
signal.setitimer(signal.ITIMER_REAL, itimer_interval)

# Wait 2*itimer_interval seconds.
time.sleep(2*itimer_interval)

# Report results.

