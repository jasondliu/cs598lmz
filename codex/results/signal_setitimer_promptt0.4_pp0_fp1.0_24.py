import signal
# Test signal.setitimer()
def handler(signum, frame):
    print "signal handler"
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)

while True:
    pass

# Test signal.setitimer()
def handler(signum, frame):
    print "signal handler"
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)

while True:
    pass

# Test signal.setitimer()
def handler(signum, frame):
    print "signal handler"
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal
