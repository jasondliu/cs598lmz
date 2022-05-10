import signal
# Test signal.setitimer() on alarm()'s callback.
# This test only works if there is a signal handler for SIGALRM.
# If no such handler is installed, the test would not finish.

import gc

def handler(*args):
    print("in handler")
    return

signal.signal(signal.SIGALRM, handler)

print("setitimer")
signal.setitimer(signal.ITIMER_REAL, 1)

print("gc.collect")
gc.collect()

print("sleep")
time.sleep(2)

print("done")
