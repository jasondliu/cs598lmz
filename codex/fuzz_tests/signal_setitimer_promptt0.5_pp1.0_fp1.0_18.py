import signal
# Test signal.setitimer() and signal.getitimer()

import sys
import time

# Make sure the test runs in a reasonable amount of time on a slow machine.
if sys.platform.startswith("os2"):
    # OS/2 has a very low resolution timer, so it takes a long time
    # for the SIGALRM signal to be delivered.
    TIMEOUT_FACTOR = 25
else:
    TIMEOUT_FACTOR = 1

def handler(signum, frame):
    print("timeout")
    sys.exit(2)

signal.signal(signal.SIGALRM, handler)

# Set an alarm.
signal.setitimer(signal.ITIMER_REAL, 0.01 * TIMEOUT_FACTOR)

# Wait for the alarm.  This should exit via the signal handler.
time.sleep(1)

# If we get here, there was no signal.
print("no signal")
sys.exit(1)
