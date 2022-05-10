import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.6)
signal.setitimer(signal.ITIMER_REAL, 0)
signal.setitimer(signal.ITIMER_REAL, 1.2)
signal.setitimer(signal.ITIMER_REAL, 0)
signal.setitimer(signal.ITIMER_REAL, 1.8)
signal.setitimer(signal.ITIMER_REAL, 0)
signal.setitimer(signal.ITIMER_REAL, 2.4)
signal.setitimer(signal.ITIMER_REAL, 0)

# Test signal.setitimer()

signal.setitimer(signal.ITIMER_PROF, 1.0, 0.5)
signal.setitimer(signal.ITIMER_PROF, 1.0, 0.75)
signal.setitimer(signal.ITIMER_PROF, 1.0, 1.
