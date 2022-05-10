import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.setitimer(signal.ITIMER_REAL, 0, 0)
signal.setitimer(signal.ITIMER_REAL, 0, 1)
signal.setitimer(signal.ITIMER_REAL, 1, 1)

# Test signal.setitimer with keyword arguments
signal.setitimer(signal.ITIMER_REAL, interval=1, value=1)
signal.setitimer(signal.ITIMER_REAL, interval=1, value=1)

# Test signal.setitimer with invalid interval
try:
    signal.setitimer(signal.ITIMER_REAL, -1, 0)
except ValueError:
    pass
else:
    print("expected ValueError")

try:
    signal.setitimer(signal.ITIMER_REAL, 0, -1)
except ValueError:
    pass
else:
    print("expected ValueError")

