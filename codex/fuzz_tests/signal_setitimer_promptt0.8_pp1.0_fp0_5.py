import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 1, 0.2)
time.sleep(1)
# Test signal.siginterrupt
signal.siginterrupt(signal.SIGCHLD, False)
# Test signal.sigisdefaul
signal.sigisdefault(signal.SIGINT)
signal.sigisdefault(signal.SIG_DFL)
# Test signal.sigset
signal.signal(signal.SIGINT, signal.SIG_DFL)
signal.sigset(signal.SIGINT, signal.SIG_DFL)
