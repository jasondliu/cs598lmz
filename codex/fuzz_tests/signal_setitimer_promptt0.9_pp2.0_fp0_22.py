import signal
# Test signal.setitimer (itimer-like timer)
# Problems on Solaris and IRIX -- see test_timing.py for test cases.
import sys, time

try:
    signal.setitimer(signal.ITIMER_VIRTUAL, 1.0, 0.0)
except AttributeError, err:
    if sys.platform[:6] == 'darwin' or sys.platform[:7] == 'freebsd':
        print 'skipped',
    else:
        raise
else:
    # Make sure that only the first signal arrives
    signal_caught = [False]
    def handler(signum, frame):
        print "handler"
        if not signal_caught[0]:
            signal_caught[0] = True
            signal.alarm(5)
        else:
            raise Exception, "too many signals"
    signal.signal(signal.SIGALRM, handler)

    if sys.platform[:6] == 'darwin':
        # Need to use SIGVTALRM if available (see darwin docs for the
        #
