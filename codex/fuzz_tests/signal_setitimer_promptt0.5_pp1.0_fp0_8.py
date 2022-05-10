import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)

# setitimer() takes seconds and microseconds as arguments.
# The first argument is the interval after which the signal
# will be sent. The second argument is the interval after
# which the next signal will be sent (if any).
signal.setitimer(signal.ITIMER_REAL, 1, 0.5)

print 'Sleeping'
signal.pause()
print 'Exiting'
