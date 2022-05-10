import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 1)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)

# Test signal.signal()
