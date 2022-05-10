import signal
# Test signal.setitimer and signal.ITIMER_REAL
signal.setitimer(signal.ITIMER_REAL, 1.23, 4.56)
s = signal.setitimer(signal.ITIMER_REAL)
assert set([1.23, 4.56]) == set(s), s
