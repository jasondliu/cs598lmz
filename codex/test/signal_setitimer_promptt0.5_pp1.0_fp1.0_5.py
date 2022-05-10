import signal
# Test signal.setitimer() and signal.getitimer()

# Make sure we can set and get the timer
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
timer = signal.getitimer(signal.ITIMER_REAL)
assert timer == (0.5, 0.5)

# Make sure we can set and get the timer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.5, 0.5)
timer = signal.getitimer(signal.ITIMER_VIRTUAL)
assert timer == (0.5, 0.5)

# Make sure we can set and get the timer
signal.setitimer(signal.ITIMER_PROF, 0.5, 0.5)
timer = signal.getitimer(signal.ITIMER_PROF)
assert timer == (0.5, 0.5)

# Make sure we get ValueError for unknown timer
