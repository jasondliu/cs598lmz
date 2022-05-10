import signal
# Test signal.setitimer()

from test_support import verbose

def handler(signum, frame):
    if verbose:
        print 'handler'

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
signal.pause()
