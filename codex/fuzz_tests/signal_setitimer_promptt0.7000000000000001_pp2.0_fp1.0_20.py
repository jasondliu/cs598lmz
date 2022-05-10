import signal
# Test signal.setitimer() and signal.getitimer().
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)
assert signal.getitimer(signal.ITIMER_REAL) == (0.1, 0.2)

print('Test getitimer (passed).')
