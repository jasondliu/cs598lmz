import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0)
signal.setitimer(signal.ITIMER_PROF, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0)

# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_PROF)
signal.getitimer(signal.ITIMER_VIRTUAL)

# Test signal.siginterrupt
signal.siginterrupt(signal.SIGINT, True)
signal.siginterrupt(signal.SIGINT, False)

# Test signal.
