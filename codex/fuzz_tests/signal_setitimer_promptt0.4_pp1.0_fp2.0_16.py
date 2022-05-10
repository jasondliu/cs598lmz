import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)

# This call sets an alarm to fire in 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# This call blocks until a signal is received
signal.pause()

print 'Returned from pause()'
