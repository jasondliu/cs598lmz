import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "Received SIGALRM"
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

while 1:
    pass
