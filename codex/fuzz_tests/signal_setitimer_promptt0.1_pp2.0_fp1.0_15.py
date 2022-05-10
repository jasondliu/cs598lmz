import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)

# This call sets an alarm to go off in 5 seconds
signal.setitimer(signal.ITIMER_REAL, 5)

# This call blocks until any signal is received
signal.pause()
