import signal
# Test signal.setitimer() with SIGALRM

import time

def handler(signum, frame):
    print "got signal", signum

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

for i in range(5):
    print "tick"
    time.sleep(0.5)

signal.setitimer(signal.ITIMER_REAL, 0)

print "done"
