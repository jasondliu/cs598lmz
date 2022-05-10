import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "signum", signum
    print "frame", frame
    print "handler"

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0, 1)

while True:
    pass
