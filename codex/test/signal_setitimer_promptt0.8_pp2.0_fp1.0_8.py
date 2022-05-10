import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
signal.setitimer(signal.ITIMER_PROF, 1, 0)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getitimer(signal.ITIMER_PROF)

# Test signal.pause()
signal.pause()
