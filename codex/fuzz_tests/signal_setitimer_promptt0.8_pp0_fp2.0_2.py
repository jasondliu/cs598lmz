import signal
# Test signal.setitimer()

def handler(sig, frame):
    print sig, frame
    signal.setitimer(signal.ITIMER_REAL, 0.5)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    pass
