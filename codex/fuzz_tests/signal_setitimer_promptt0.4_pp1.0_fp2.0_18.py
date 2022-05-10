import signal
# Test signal.setitimer
# This test is not very good, because it is not clear what the
# exact timing should be.  It is used to check that the signal
# is delivered at about the right time.

import time

def handler(signum, frame):
    print 'handler'
    signal.setitimer(signal.ITIMER_REAL, 0.1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

time.sleep(0.5)
