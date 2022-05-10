import signal
# Test signal.setitimer()
# Note: this test may fail on some platforms since it relies on
# implementation details of the Python signal module.

def handler(signum, frame):
    pass

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.2)
signal.setitimer(signal.ITIMER_REAL, 0.3)
signal.setitimer(signal.ITIMER_REAL, 0.4)
signal.setitimer(signal.ITIMER_REAL, 0.5)
signal.setitimer(signal.ITIMER_REAL, 0.6)
signal.setitimer(signal.ITIMER_REAL, 0.7)
signal.setitimer(signal.ITIMER_REAL, 0.8)
signal.setitimer(signal.ITIMER_REAL, 0.9)
