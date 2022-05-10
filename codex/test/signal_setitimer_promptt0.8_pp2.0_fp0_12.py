import signal
# Test signal.setitimer() when itimer is not set

def handler(signum, frame):
    #print "signal %d received" % signum
    pass

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.0)

