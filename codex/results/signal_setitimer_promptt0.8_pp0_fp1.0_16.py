import signal
# Test signal.setitimer and signal.getitimer.
# I expect this to hang for 120 seconds, until the timer expires.
def handler(signum, frame):
    print "*** Timeout!"
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 120);
signal.getitimer(signal.ITIMER_REAL)
