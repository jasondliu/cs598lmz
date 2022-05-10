import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.0)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.0)
signal.setitimer(signal.ITIMER_REAL, 0.1, 1.0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 1.0)
signal.setitimer(signal.ITIMER_PROF, 0.1, 1.0)
signal.setitimer(signal.ITIMER_REAL, 0.0, 0.0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.0, 0.0)
signal.setitimer(signal.ITIMER_PROF, 0.0, 0.0)
