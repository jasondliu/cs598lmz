import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
while True:
    signal.pause()

# Test signal.setitimer with a signal handler
def handler(signum, frame):
    print("Signal", signum, "received")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
while True:
    signal.pause()
