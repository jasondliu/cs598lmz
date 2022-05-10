import signal
# Test signal.setitimer
#
# Note that this test can be run only once in a process.

import sys
import time

def handler(signum, frame):
    print("signal", signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

while True:
    try:
        time.sleep(1.0)
    except KeyboardInterrupt:
        print("good bye")
        sys.exit(0)
