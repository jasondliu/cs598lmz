import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 1, 0.5)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0.5)
signal.setitimer(signal.ITIMER_PROF, 1, 0.5)
# Test signal.set_wakeup_fd
signal.set_wakeup_fd(1)
# Test signal.siginterrupt
signal.siginterrupt(signal.SIGINT, False)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getitimer(signal.ITIMER_PROF)
# Test signal.pause
signal.pause()
# Test signal.signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_IGN)
# Test signal.getsign
