import signal
# Test signal.setitimer()

# TODO: Remove this once the test is complete.
signal.signal(signal.SIGALRM, signal.default_int_handler)
signal.alarm(1)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getit
