import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Test signal.getitimer()
print(signal.getitimer(signal.ITIMER_REAL))

# Test signal.alarm()
signal.alarm(1)

# Test signal.setitimer() with negative values
signal.setitimer(signal.ITIMER_REAL, -1, -1)

# Test signal.getitimer()
print(signal.getitimer(signal.ITIMER_REAL))

# Test signal.alarm() with negative values
signal.alarm(-1)
