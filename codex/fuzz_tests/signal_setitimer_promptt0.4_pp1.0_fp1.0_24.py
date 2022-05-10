import signal
# Test signal.setitimer() and signal.getitimer()

import time
import os

def handler(signum, frame):
    print "handler"

signal.signal(signal.SIGALRM, handler)

print "setting itimer"
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while 1:
    time.sleep(1)
    print "tick"
