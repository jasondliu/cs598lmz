import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)

# Test signal.setitimer
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

try:
    signal.setitimer(-1, 0.1, 0.1)
except ValueError:
    pass

try:
    signal.setitimer(signal.ITIMER_REAL, -1, 0.1)
except ValueError:
    pass

try:
    signal.setitimer(signal.ITIMER_REAL, 0.1, -1)
except ValueError:
    pass

# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)

signal.getitimer(signal.ITIMER_VIRTUAL)

signal.getitimer
