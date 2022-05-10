import signal
# Test signal.setitimer value
# Test signal.setitimer value
signal.setitimer(signal.ITIMER_VIRTUAL, 2)
signal.setitimer(signal.ITIMER_REAL, 2)
signal.setitimer(signal.ITIMER_PROF, 2)

# Test signal.getitimer value
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_PROF)

# Test signal.signal value
signal.signal(signal.SIGABRT, signal.SIG_DFL)
signal.signal(signal.SIGALRM, signal.SIG_DFL)
signal.signal(signal.SIGBUS, signal.SIG_DFL)
signal.signal(signal.SIGCHLD, signal.SIG_DFL)
