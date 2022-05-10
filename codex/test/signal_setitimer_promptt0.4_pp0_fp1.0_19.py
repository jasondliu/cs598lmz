import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.2)
signal.setitimer(signal.ITIMER_PROF, 0.3)
signal.setitimer(signal.ITIMER_REAL, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0)
signal.setitimer(signal.ITIMER_PROF, 0)
# Test signal.setitimer with negative value
signal.setitimer(signal.ITIMER_REAL, -1)
signal.setitimer(signal.ITIMER_VIRTUAL, -1)
signal.setitimer(signal.ITIMER_PROF, -1)
# Test signal.setitimer with invalid value
try:
    signal.setitimer(signal.ITIMER_REAL, 'a')
except TypeError:
    pass
