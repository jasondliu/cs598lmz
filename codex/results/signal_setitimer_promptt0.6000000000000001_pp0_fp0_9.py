import signal
# Test signal.setitimer
def timeout(signum, frame):
    print 'signal %d' % signum

signal.signal(signal.SIGALRM, timeout)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    print 'waiting'
    time.sleep(1)


# Test signal.setitimer
def timeout(signum, frame):
    print 'signal %d' % signum

signal.signal(signal.SIGALRM, timeout)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    print 'waiting'
    time.sleep(1)

# Test signal.signal
def timeout(signum, frame):
    print 'signal %d' % signum

signal.signal(signal.SIGALRM, timeout)
signal.alarm(1)

while True:
    print 'waiting'
    time.sleep(1)

