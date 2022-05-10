import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 1, 2)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 2)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_PROF, 1, 2)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_VIRTUAL)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_PROF)

# Test signal.getsignal()
signal.getsignal(signal.SIGUSR1)

# Test signal.setsignal()
signal.setsignal(signal.SIGUSR1, signal.SIG_IGN)

# Test signal.getsignal()
