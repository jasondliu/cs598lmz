import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 1, 1)
time.sleep(2)
signal.setitimer(signal.ITIMER_REAL, 0)

signal.setitimer(signal.ITIMER_VIRTUAL, 1, 1)
time.sleep(2)
signal.setitimer(signal.ITIMER_VIRTUAL, 0)

signal.setitimer(signal.ITIMER_PROF, 1, 1)
time.sleep(2)
signal.setitimer(signal.ITIMER_PROF, 0)

# Test signal.getitimer
signal.setitimer(signal.ITIMER_REAL, 1, 2)
assert signal.getitimer(signal.ITIMER_REAL) == (1, 2)
signal.setitimer(signal.ITIMER_REAL, 0)

signal.setitimer(signal.ITIMER_VIRTUAL, 1, 2)
assert signal.getit
