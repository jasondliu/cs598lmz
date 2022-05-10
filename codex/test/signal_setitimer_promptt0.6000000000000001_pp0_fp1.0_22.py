import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.5, 1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.5, 1)
signal.setitimer(signal.ITIMER_PROF, 0.5, 1)

