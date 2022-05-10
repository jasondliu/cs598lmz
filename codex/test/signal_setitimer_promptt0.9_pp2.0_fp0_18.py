import signal
# Test signal.setitimer() and signal.setitimer()
def handler(signum, frame):
    pass

signal.setitimer(signal.ITIMER_REAL, 1, 2)
