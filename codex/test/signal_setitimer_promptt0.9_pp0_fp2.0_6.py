import signal
# Test signal.setitimer and signal.getitimer
# See if SIGILL is generated:
signal.signal(signal.SIGILL, signal.SIG_IGN)
signal.setitimer(signal.ITIMER_REAL, 0, 1)
signal.getitimer(signal.ITIMER_REAL)
signal.setitimer(signal.ITIMER_VIRTUAL, 0, 1)
signal.getitimer(signal.ITIMER_VIRTUAL)
