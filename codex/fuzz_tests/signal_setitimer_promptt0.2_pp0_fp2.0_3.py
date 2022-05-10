import signal
# Test signal.setitimer()
#
# This test is not very good, since it depends on the system clock.
# It will fail if the system clock is changed during the test.

import signal, time

def handler(signum, frame):
    print 'handler'
    raise SystemExit

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.2)

print 'done'
