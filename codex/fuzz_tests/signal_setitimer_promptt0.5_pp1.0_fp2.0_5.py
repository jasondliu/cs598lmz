import signal
# Test signal.setitimer:

def handler(signum, frame):
    print("got SIGALRM")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5)

# This should process signals,
# even though it's a busy loop.
while True:
    pass

# This should print "got SIGALRM" after
# about half a second.

# Test signal.setitimer:

def handler(signum, frame):
    print("got SIGALRM")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5)

# This should process signals,
# even though it's a busy loop.
while True:
    pass

# This should print "got SIGALRM" after
# about half a second.

 
# Test signal.setitimer:

def handler(signum, frame):
    print("got SIGALRM")

signal.signal
