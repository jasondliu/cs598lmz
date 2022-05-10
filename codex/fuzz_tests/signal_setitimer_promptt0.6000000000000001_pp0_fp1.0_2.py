import signal
# Test signal.setitimer
signal.signal(signal.SIGALRM, signal.SIG_IGN)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0)
signal.setitimer(signal.ITIMER_PROF, 0)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getitimer(signal.ITIMER_PROF)
# Test signal.set_wakeup_fd
signal.set_wakeup_fd(1)
# Test signal.set_
