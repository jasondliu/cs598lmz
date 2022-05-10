import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.05, 0.05)
signal.alarm(5)

