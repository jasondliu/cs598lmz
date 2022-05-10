import signal
# Test signal.setitimer
#
# This test starts a subprocess and sends it a series of SIGALRM's.  The
# subprocess runs a loop that measures the time between SIGALRM's.  If the
# times are too small, the child exits with an error.  If they are too large,
# the child exits with another error.
#
# The goal is to measure the resolution of setitimer.  The current
# implementation is limited to a 10 millisecond resolution, and this test
# depends on that.

TIMEOUT = 0.2

def handler(signum, frame):
    if signum != signal.SIGALRM:
        print("in handler: wrong signal:", signum)
        sys.exit(2)

def child(nloops):
    signal.signal(signal.SIGALRM, handler)
    start = time.time()
    signal.setitimer(signal.ITIMER_REAL, TIMEOUT, 0)
    while 1:
        delta = time.time() - start
