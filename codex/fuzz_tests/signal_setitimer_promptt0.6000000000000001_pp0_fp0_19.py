import signal
# Test signal.setitimer()

def handler(signum, frame):
    sys.exit()

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0)
signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.setitimer(signal.ITIMER_REAL, 0, 0)

signal.setitimer(signal.ITIMER_VIRTUAL, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)

signal.setitimer(signal.ITIMER_PROF, 0)
signal.setitimer(signal.ITIMER_PROF,
