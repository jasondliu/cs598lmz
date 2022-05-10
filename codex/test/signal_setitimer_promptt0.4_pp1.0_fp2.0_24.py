import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1)

try:
    # Test signal.setitimer()
    signal.setitimer(signal.ITIMER_REAL, 0.1)
except ValueError:
    pass

try:
    # Test signal.setitimer()
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
except ValueError:
    pass

try:
    # Test signal.setitimer()
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1, 0.1)
except TypeError:
    pass

try:
    # Test signal.setitimer()
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1, 0.1, 0.1)
except TypeError:
    pass

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)

