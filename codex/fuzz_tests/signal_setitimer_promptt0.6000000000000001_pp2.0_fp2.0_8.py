import signal
# Test signal.setitimer

def handler(signum, frame):
    print 'received signal', signum, 'at', frame
    if signum == signal.SIGALRM:
        raise KeyboardInterrupt

signal.signal(signal.SIGALRM, handler)
print 'starting timer'
signal.setitimer(signal.ITIMER_REAL, 1, 0)
try:
    print 'looping'
    while True: pass
except KeyboardInterrupt:
    print 'caught keyboard interrupt in loop'

signal.setitimer(signal.ITIMER_REAL, 0)
print 'done'
