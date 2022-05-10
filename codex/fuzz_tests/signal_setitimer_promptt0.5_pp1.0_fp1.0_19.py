import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "Handler called with signal", signum
    signal.setitimer(signal.ITIMER_REAL, 1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

while True:
    pass
