import signal
# Test signal.setitimer
# This test passes by not crashing.
signal.setitimer(signal.ITIMER_VIRTUAL, 0.5, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0)

# Test signal.setitimer with invalid first argument
try:
    signal.setitimer(5, 0.5, 0)
except ValueError:
    pass
else:
    raise RuntimeError("setitimer didn't raise ValueError")

# Test signal.setitimer with invalid second argument
try:
    signal.setitimer(signal.ITIMER_VIRTUAL, 'five', 0)
except TypeError:
    pass
else:
    raise RuntimeError("setitimer didn't raise TypeError")

# Test signal.setitimer with invalid third argument
try:
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.5, 'five')
except TypeError:
    pass
else:
    raise RuntimeError("setitimer didn't raise TypeError")
