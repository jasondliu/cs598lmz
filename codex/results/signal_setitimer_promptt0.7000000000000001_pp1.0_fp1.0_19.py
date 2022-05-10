import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 1, 2)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 2)
signal.setitimer(signal.ITIMER_PROF, 1, 2)
signal.setitimer(-1, 1, 2) # TypeError
