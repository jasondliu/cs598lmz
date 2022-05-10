import signal
# Test signal.setitimer at all
signal.setitimer
# Test signal.setitimer from python
signal.setitimer (None, None, None)
signal.setitimer (signal.ITIMER_PROF, 1e-6, 2)
signal.setitimer (signal.ITIMER_REAL, 1e-8, 2)
signal.setitimer (signal.ITIMER_VIRTUAL, 2, 4)
signal.setitimer ('SIGPROF', 1e-6, 2)
signal.setitimer ('SIGALRM', 1e-8, 2)
signal.setitimer ('SIGVTALRM', 2, 4)
signal.setitimer (signal.ITIMER_REAL, 1e-8, 0)
# Test signal.getitimer
signal.getitimer (signal.ITIMER_REAL)
# Test signal.alarm
signal.alarm
