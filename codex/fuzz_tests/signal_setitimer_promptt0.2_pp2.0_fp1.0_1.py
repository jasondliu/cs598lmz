import signal
# Test signal.setitimer()
#
# This test is not very good, because it relies on the timer
# expiring while the test is running.  If the test runs too fast,
# the timer will expire before the test starts.  If the test runs
# too slow, the timer will expire after the test finishes.
#
# It's not clear how to fix this.  The test could sleep for a
# while, but it would be hard to know how long to sleep.

import signal
import sys

def handler(signum, frame):
    print('handler called')
    sys.exit(0)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1)

print('waiting for timer to expire')
while True:
    pass
