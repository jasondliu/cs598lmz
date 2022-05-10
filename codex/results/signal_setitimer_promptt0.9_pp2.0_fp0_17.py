import signal
# Test signal.setitimer.
signal.setitimer(signal.ITIMER_REAL, 1.24, 5.27)
signal.setitimer(signal.ITIMER_VIRTUAL, 1.24, 5.27)
signal.setitimer(signal.ITIMER_PROF, 1.24, 5.27)
signal.setitimer(-1, 1.24, 5.27)  # There's no such signal, but validate the args.
signal.setitimer(signal.ITIMER_REAL)
signal.setitimer(signal.ITIMER_REAL, 1.24)
signal.setitimer(42, 1.24, 5.27)
signal.setitimer(signal.ITIMER_REAL, 'x', 5.27)
signal.setitimer(signal.ITIMER_REAL, 1.24, 'x')
signal.setitimer(signal.ITIMER_REAL, (1.0, 2.0), 5.27)
signal.setit
