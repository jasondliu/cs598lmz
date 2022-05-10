import signal
# Test signal.setitimer to verify that it works
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)
# The signal handler.
