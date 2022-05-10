import signal
# Test signal.setitimer()
#
# This test is a bit tricky, because we need to make sure that the
# signal handler is called before the itimer expires.  We do this by
# setting the itimer to a very short time, and then making sure that
# the signal handler is called before the itimer expires.

def handler(signum, frame):
    print "handler called"
    sys.exit(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while 1:
    pass
