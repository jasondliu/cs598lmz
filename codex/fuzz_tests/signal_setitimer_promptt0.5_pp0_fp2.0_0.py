import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 1.0)
signal.setitimer(signal.ITIMER_REAL, 0.0)
signal.setitimer(signal.ITIMER_VIRTUAL, 1.0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.0)
signal.setitimer(signal.ITIMER_PROF, 1.0)
signal.setitimer(signal.ITIMER_PROF, 0.0)
try:
    signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)
    signal.setitimer(signal.ITIMER_REAL, 0.0, 1.0)
    signal.setitimer(signal.ITIMER_VIRTUAL, 1.0, 0.0)
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.0, 1.0)
    signal.setitimer(signal.ITIM
