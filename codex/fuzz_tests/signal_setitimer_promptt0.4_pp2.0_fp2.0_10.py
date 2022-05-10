import signal
# Test signal.setitimer()
import sys

def handler(signum, frame):
    print "handler"
    sys.exit(1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    pass
