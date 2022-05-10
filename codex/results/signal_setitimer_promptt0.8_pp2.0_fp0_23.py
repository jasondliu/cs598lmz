import signal
# Test signal.setitimer, using SIGALRM for the timer signal.

import os
import time

def handler(signum, frame):
    global handler_calls
    handler_calls += 1
    time.sleep(1)

signal.signal(signal.SIGALRM, handler)

handler_calls = 0

time.sleep(1)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(1.5)
signal.setitimer(signal.ITIMER_REAL, 0, 0)

# We expect three calls: two from the first timer and one from the second.
assert handler_calls == 3
