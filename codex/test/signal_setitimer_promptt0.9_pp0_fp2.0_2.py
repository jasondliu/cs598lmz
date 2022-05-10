import signal
# Test signal.setitimer call
signal.setitimer(signal.ITIMER_PROF, 0.001, 0.001)
# or
signal.setitimer(signal.ITIMER_REAL, 0.001, 0.001)
