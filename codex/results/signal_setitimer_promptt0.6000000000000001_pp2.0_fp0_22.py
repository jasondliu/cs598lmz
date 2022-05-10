import signal
# Test signal.setitimer() with a realtime signal.
import sys, time

from test_support import verify

signal.signal(signal.SIGALRM, lambda signum, frame: sys.exit(0))
signal.setitimer(signal.ITIMER_REAL, 1, 0)
time.sleep(2)
verify(False)
