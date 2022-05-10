import signal
# Test signal.setitimer

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.signal(signal.SIGALRM, lambda signum, frame: None)
signal.pause()
