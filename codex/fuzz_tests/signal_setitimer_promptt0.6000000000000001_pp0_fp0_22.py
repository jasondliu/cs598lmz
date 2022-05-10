import signal
# Test signal.setitimer().
# This is supposed to raise a SIGALRM after the specified number of seconds
# have elapsed.  Note that the timer may go off "early"; i.e. we can't expect
# the process to be suspended for exactly the right amount of time.

import time
import sys

def handler(signum, frame):
    print("handler invoked")
    sys.exit(0)

signal.signal(signal.SIGALRM, handler)

print("setting alarm")
signal.setitimer(signal.ITIMER_REAL, 2)

print("pausing")
time.sleep(5)
print("time's up")
