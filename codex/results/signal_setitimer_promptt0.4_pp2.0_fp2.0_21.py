import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)

# Test signal.alarm()
signal.alarm(2)

# Test signal.pause()
signal.pause()
