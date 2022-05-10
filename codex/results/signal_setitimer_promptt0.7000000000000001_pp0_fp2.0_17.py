import signal
# Test signal.setitimer implementation
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

def handler(signum, frame):
    print "Got SIGALRM"

signal.signal(signal.SIGALRM, handler)

# This is needed to handle the SIGALRM within Python
while True:
    signal.pause()

# Test signal.setitimer implementation
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

def handler(signum, frame):
    print "Got SIGALRM"

signal.signal(signal.SIGALRM, handler)

# This is needed to handle the SIGALRM within Python
while True:
    signal.pause()

# Test signal.setitimer implementation
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

def handler(signum, frame):
    print "Got SIGALRM"

signal.signal(signal.SIGALRM,
