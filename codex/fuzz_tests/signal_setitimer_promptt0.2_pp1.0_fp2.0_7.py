import signal
# Test signal.setitimer()
#
# This test is not very good, because it doesn't actually test the
# timer.  It just tests that the signal handler is called.

def handler(signum, frame):
    print "handler called"
    raise SystemExit

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

while 1:
    pass
