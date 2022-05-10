import signal
# Test signal.setitimer()

def handler(signum, frame):
    print(signum, frame)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0.5)

while True:
    pass
