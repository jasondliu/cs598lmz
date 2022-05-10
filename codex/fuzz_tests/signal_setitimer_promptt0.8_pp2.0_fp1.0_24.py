import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print "handler called for signum", signum

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

sleep(3.1415)
