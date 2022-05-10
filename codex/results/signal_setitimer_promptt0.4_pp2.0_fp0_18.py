import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.2)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.3)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_VIRTUAL, 0.2)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_VIRTUAL, 0.2, 0.3)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_PROF, 0.2)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_PROF, 0.2, 0.3)
