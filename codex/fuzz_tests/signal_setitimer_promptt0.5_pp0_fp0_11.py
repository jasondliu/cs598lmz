import signal
# Test signal.setitimer()

import time

def handler(signum, frame):
    print "Got signal", signum, "at", time.time()

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 2, 1)
while True:
    pass
