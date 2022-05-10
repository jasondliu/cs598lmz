import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0)
signal.setitimer(signal.ITIMER_REAL, 0, 30)
signal.setitimer(signal.ITIMER_REAL, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 30)

signal.setitimer(signal.ITIMER_VIRTUAL, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0, 30)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 30)

signal.setitimer(signal.ITIMER_PROF, 0)
signal.setitimer(signal.ITIMER_PROF, 0, 30)
signal.setitimer(signal.ITIMER_PROF, 0.1)
