import signal
# Test signal.setitimer
import os
import sys
import time

def handler(signum, frame):
    print('received signal', signum)
    sys.stdout.flush()

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGVTALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.3, 0.3)
signal.setitimer(signal.ITIMER_PROF, 0.4, 0.4)

time.sleep(1.0)

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.3, 0.3)
signal.setitimer(signal.ITIMER_PROF, 0.4, 0.4)

time.sleep(1.0)


