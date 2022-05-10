import signal
# Test signal.setitimer() and signal.getitimer().

signal.alarm(1)

print signal.getitimer(signal.ITIMER_REAL)
print signal.getitimer(signal.ITIMER_VIRTUAL)
print signal.getitimer(signal.ITIMER_PROF)

def handler(signum, frame):
    print 'handler called'
    print signal.getitimer(signal.ITIMER_REAL)
    print signal.getitimer(signal.ITIMER_VIRTUAL)
    print signal.getitimer(signal.ITIMER_PROF)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)
