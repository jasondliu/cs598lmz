import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print("got signal", signum)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

signal.setitimer(signal.ITIMER_REAL, 0)
