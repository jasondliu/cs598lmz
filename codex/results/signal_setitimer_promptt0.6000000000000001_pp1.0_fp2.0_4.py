import signal
# Test signal.setitimer()

def signal_handler(signum, frame):
    print "got signal", signum

signal.signal(signal.SIGALRM, signal_handler)

signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

while 1:
    pass
