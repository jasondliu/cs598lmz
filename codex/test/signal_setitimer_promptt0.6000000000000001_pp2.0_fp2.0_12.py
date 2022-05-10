import signal
# Test signal.setitimer() and signal.getitimer()
signal.setitimer(signal.ITIMER_REAL, 1)
print(signal.getitimer(signal.ITIMER_REAL))
signal.setitimer(signal.ITIMER_REAL, 1)
print(signal.getitimer(signal.ITIMER_REAL))

# This should raise an exception
try:
    signal.setitimer(signal.ITIMER_REAL, 1, 2)
except ValueError as e:
    print(e)

# Test signal.setitimer() and signal.getitimer()
signal.setitimer(signal.ITIMER_VIRTUAL, 1)
print(signal.getitimer(signal.ITIMER_VIRTUAL))
signal.setitimer(signal.ITIMER_VIRTUAL, 1)
print(signal.getitimer(signal.ITIMER_VIRTUAL))

# This should raise an exception
