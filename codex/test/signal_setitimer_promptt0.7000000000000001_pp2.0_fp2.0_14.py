import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_PROF, 0.1)

signal.setitimer(signal.ITIMER_REAL, 1.0)

signal.setitimer(signal.ITIMER_VIRTUAL, 0.5)

signal.setitimer(-1, 0.1)

