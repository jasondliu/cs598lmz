import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
signal.setitimer(signal.ITIMER_REAL, 2, 0)
signal.setitimer(signal.ITIMER_PROF, 3, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 1)
signal.setitimer(signal.ITIMER_REAL, 2)
signal.setitimer(signal.ITIMER_PROF, 3)
# Test signal.getsignal
signal.getsignal(signal.SIGINT)
signal.getsignal(signal.SIGTERM)
signal.getsignal(signal.SIGKILL)
# Test signal.setitimer
signal.signal(signal.SIGINT, signal.SIG_DFL)
signal.signal(signal.SIGTERM, signal.SIG_DFL)
