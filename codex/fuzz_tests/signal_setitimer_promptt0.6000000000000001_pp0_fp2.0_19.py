import signal
# Test signal.setitimer

signal.signal(signal.SIGALRM, lambda x, y: None)
signal.setitimer(signal.ITIMER_REAL, 0, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0, 0.1)

signal.setitimer(signal.ITIMER_REAL, 0, 0.1)
