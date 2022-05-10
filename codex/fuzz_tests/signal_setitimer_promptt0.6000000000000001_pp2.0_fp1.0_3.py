import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "Signal", signum, "received"

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.5)

# This will loop until a SIGALRM is received.
while True:
    pass
