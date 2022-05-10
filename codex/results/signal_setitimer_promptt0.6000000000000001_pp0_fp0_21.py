import signal
# Test signal.setitimer()

# This is a simple test of signal.setitimer().

# The program sets a timer and sleeps.  When it wakes up, it checks
# that the timer expired.

# This test requires a system that supports itimers.

import time
import signal
import os

# Check whether this test is applicable.
if not hasattr(signal, 'setitimer'):
    raise ImportError("This system does not support setitimer()")

def handler(signum, frame):
    print 'handler'
    raise SystemExit

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1.0)
print 'before sleep'
time.sleep(2)
print 'after sleep'

# The program should never reach this point.
raise SystemError("setitimer() did not work")
