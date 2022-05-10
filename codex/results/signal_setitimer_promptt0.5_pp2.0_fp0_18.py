import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 1.0, 0.5)
signal.setitimer(signal.ITIMER_PROF, 1.0, 0.5)
signal.setitimer(signal.ITIMER_VIRTUAL, 1.0, 0.5)

# Test signal.signal
def handler(signum, frame):
    pass
signal.signal(signal.SIGABRT, handler)
signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGBUS, handler)
signal.signal(signal.SIGCHLD, handler)
signal.signal(signal.SIGCONT, handler)
signal.signal(signal.SIGFPE, handler)
signal.signal(signal.SIGHUP, handler)
signal.signal(signal.SIGILL, handler)
signal.signal(signal.SIGINT, handler)
signal.signal(signal
