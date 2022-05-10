import signal
# Test signal.setitimer() with alarm().
signal.signal(signal.SIGALRM, lambda sig, frame: None)
signal.setitimer(signal.ITIMER_REAL, 1, 1)
signal.alarm(1)
signal.setitimer(signal.ITIMER_REAL, 1, 1)
signal.alarm(1)
