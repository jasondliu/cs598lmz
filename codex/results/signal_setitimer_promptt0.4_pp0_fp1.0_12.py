import signal
# Test signal.setitimer() with SIGALRM

def handler(signum, frame):
    print "handler"
    raise RuntimeError("timeout")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

try:
    while True:
        pass
except RuntimeError, e:
    print e
    pass
