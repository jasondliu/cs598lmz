import signal
# Test signal.setitimer()

# This test is a bit tricky to get right, because it's not easy to
# tell if the signal handler was called at the right time.  So we
# just do a few iterations of the test, and hope we get lucky.

import signal
import time

def handler(signum, frame):
    global count
    count += 1
    print 'handler called'

count = 0
signal.signal(signal.SIGALRM, handler)

for i in range(10):
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
    time.sleep(0.2)
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
    time.sleep(0.1)
    print count
    if count != 2:
        print 'wrong count'
    count = 0

print 'done'
