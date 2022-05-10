import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

signal.signal(signal.SIGALRM, handler)

# This should cause the signal handler to be called every 5 seconds
signal.setitimer(signal.ITIMER_REAL, 5, 5)

while True:
    pass
