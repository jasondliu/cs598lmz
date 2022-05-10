import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.5, 0.0)
signal.setitimer(signal.ITIMER_PROF, 0.5, 0.0)

# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getitimer(signal.ITIMER_PROF)

# Test signal.signal
signal.signal(signal.SIGALRM, handler)

# Test signal.siginterrupt
signal.siginterrupt(signal.SIGALRM, True)
signal.siginterrupt(signal.SIGALRM, False)

# Test signal.getsignal
signal.getsignal(signal.SIGALRM)

# Test signal.set_wakeup_fd
signal
