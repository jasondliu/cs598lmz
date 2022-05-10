import signal
# Test signal.setitimer() on Python 3.5

import support

try:
    signal.setitimer(signal.ITIMER_REAL, 1, 0)
except:
    raise support.TestError("setitimer() not supported")

def Abort(signum, frame):
    raise support.TestError("Time limit exceeded")

signal.signal(signal.SIGALRM, Abort)
signal.setitimer(signal.ITIMER_REAL, 0.01, 0)

import time
time.sleep(2)
