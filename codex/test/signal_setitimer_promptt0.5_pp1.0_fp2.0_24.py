import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.2)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.2)

# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getitimer(signal.ITIMER_PROF)

# Test signal.signal
def handler(signum, frame):
    pass

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGILL, handler)
signal.signal(signal.SIGABRT, handler)
signal.signal(signal.SIGBUS, handler)
