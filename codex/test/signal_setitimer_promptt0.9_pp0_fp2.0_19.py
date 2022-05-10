import signal
# Test signal.setitimer
interval = 3
signal.setitimer(signal.ITIMER_REAL, interval)
i = 1
