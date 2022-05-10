import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal", signum, "caught")

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1)

while True:
    pass
