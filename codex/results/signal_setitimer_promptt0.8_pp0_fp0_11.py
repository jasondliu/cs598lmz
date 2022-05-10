import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "timeout"
    sys.exit()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)

while True:
    pass
