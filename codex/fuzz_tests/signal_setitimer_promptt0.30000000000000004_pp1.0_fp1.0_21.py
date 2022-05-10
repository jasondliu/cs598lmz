import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "Got signal", signum

signal.signal(signal.SIGALRM, handler)

# setitimer() takes a timeval as the first arg
# timeval is a tuple of two ints, seconds and microseconds
# setitimer() takes an optional second arg, which is the interval
# between subsequent signals
signal.setitimer(signal.ITIMER_REAL, (1, 0))

while True:
    pass
