import signal
# Test signal.setitimer
def handle(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

signal.signal(signal.SIGALRM, handle)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Test signal.setitimer
def handle(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

signal.signal(signal.SIGALRM, handle)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Test signal.setitimer
def handle(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("
