import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getitimer(signal.ITIMER_PROF)

# Test signal.signal
signal.signal(signal.SIGALRM, signal.SIG_DFL)
signal.signal(signal.SIGALRM, signal.SIG_IGN)
signal.signal(signal.SIGALRM, signal.default_int_handler)

# Test signal.getsignal
signal.getsignal(signal.SIGALRM)

# Test signal.pause
signal.pause
