import signal
# Test signal.setitimer()
# Without python 3.2 bug (see test_setitimer_bug.py for bug
# details).

# This test doesn't currently work on Windows (see #6678)
import sys
if sys.platform == 'win32':
    raise SystemExit("Test skipped")

import time

def handler(signal_number, frame):
    pass

signal.signal(signal.SIGALRM, handler)

# Enable the interval timer
signal.setitimer(signal.ITIMER_REAL, 1, 1)

print("Enable the interval timer")
time.sleep(2)
try:
    # Disable the interval timer
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
    print("Disable the interval timer")
    time.sleep(2)
except KeyboardInterrupt:
    print("Caught SIGINT")

    # Disable the interval timer
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
    print("Disable the interval timer")
    raise

