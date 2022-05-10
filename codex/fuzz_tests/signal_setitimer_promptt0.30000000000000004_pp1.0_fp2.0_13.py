import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "handler"
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0)

while True:
    pass
