import signal
# Test signal.setitimer
import os

def sig_handler(signum, frame):
    print("Got signal:", signum)
    raise KeyboardInterrupt

signal.signal(signal.SIGALRM, sig_handler)
signal.signal(signal.SIGVTALRM, sig_handler)

secs = 0.25
# On Mac OS X 10.6, we were seeing SIGVTALRM and SIGALRM mixed up at 0.25s
# intervals.  This may be a kernel bug, but the test should be future-proof
# against any other possible bugs in other kernel versions.
signal.setitimer(signal.ITIMER_REAL, secs, secs)
signal.setitimer(signal.ITIMER_VIRTUAL, secs, secs)
