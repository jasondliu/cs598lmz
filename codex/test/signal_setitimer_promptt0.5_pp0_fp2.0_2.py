import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0, 0.1)
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0)
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_VIRTUAL)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_PROF)
# Test signal.alarm
signal.alarm(0)
# Test signal.alarm
signal.alarm(1)
# Test signal.getpid
signal.getpid()
# Test signal.getsignal
signal.getsignal(signal.SIGALRM)
