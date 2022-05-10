import signal
# Test signal.setitimer
#
# This test is not part of the test suite as it is not guaranteed to work on all
# platforms.

import time

def handler(signum, frame):
    print("Got signal", signum)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

try:
    time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
