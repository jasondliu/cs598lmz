import signal
# Test signal.setitimer() with the ITIMER_REAL timer.

from test_support import verbose
import time

if verbose:
    def alarm_handler(signum, frame):
        print 'signal', signum, 'at', time.time()

signal.signal(signal.SIGALRM, alarm_handler)

if verbose:
    print 'setitimer(ITIMER_REAL, 1.0)'
signal.setitimer(signal.ITIMER_REAL, 1.0)

if verbose:
    print 'Sleeping for 3 seconds'
time.sleep(3)

if verbose:
    print 'setitimer(ITIMER_REAL, 0)'
signal.setitimer(signal.ITIMER_REAL, 0)

if verbose:
    print 'Sleeping for 3 seconds'
time.sleep(3)
