import signal
# Test signal.setitimer()

signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.signal(signal.SIGALRM, lambda *args: None)
signal.pause()

# Test signal.setitimer() with a negative value

signal.setitimer(signal.ITIMER_REAL, -1, 0)
signal.signal(signal.SIGALRM, lambda *args: None)
signal.pause()

# Test signal.setitimer() with a negative value

signal.setitimer(signal.ITIMER_REAL, -2, 0)
signal.signal(signal.SIGALRM, lambda *args: None)
signal.pause()

# Test signal.setitimer() with a negative value

signal.setitimer(signal.ITIMER_REAL, -3, 0)
signal.signal(signal.SIGALRM, lambda *args: None)
signal.pause()

# Test signal.setitimer()
