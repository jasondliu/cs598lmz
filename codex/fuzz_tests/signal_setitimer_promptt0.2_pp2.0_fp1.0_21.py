import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)

# This call sets an alarm to go off in 5 seconds
signal.setitimer(signal.ITIMER_REAL, 5)

# This call sets an alarm to go off in 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# This call reads any pending signals, and calls the handlers.
signal.pause()
