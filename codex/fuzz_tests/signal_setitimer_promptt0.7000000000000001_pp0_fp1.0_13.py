import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "got alarm signal", signum

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1.0)
while True:
    signal.pause()
