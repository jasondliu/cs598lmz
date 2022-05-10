import signal
# Test signal.setitimer()
#
# This test is not very good.  It just runs for a while and checks that
# the timer is working.

import time

def handler(signum, frame):
    print 'handler'

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(2)

signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(2)

signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(2)

signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(2)

signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(2)

signal.setitimer(signal.ITIMER_REAL,
