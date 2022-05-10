import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)
# Test signal.getitimer()
signal.getitimer(signal.ITIMER_VIRTUAL)
# Test signal.getitimer()
signal.getitimer(signal.ITIMER_PROF)

# Test signal.signal()
signal.signal(signal.SIGALRM, signal.SIG_DFL)
# Test signal.signal()
signal.signal(signal.SIGINT, signal.SIG_IGN)

# Test signal.getsignal()
signal.
