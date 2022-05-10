import signal
# Test signal.setitimer and signal.getitimer
# Should return the old value of the timer

# Set the timer and check the return value
old_value = signal.setitimer(signal.ITIMER_REAL, 1.0, 0.5)
assert old_value == (0, 0)

# Get the timer and check the return value
new_value = signal.getitimer(signal.ITIMER_REAL)
assert new_value == (1.0, 0.5)

# Set the timer and check the return value
old_value = signal.setitimer(signal.ITIMER_REAL, 0, 0)
assert old_value == (1.0, 0.5)

# Get the timer and check the return value
new_value = signal.getitimer(signal.ITIMER_REAL)
assert new_value == (0, 0)

# Check the return value of timer before it's set
assert signal.getitimer(signal.ITIMER_VIRTUAL) == (0, 0)
assert signal.getitimer(signal
