import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 200)
signal.setitimer(signal.ITIMER_PROF, 200)
signal.setitimer(signal.ITIMER_VIRTUAL, 200)

# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_PROF)
signal.getitimer(signal.ITIMER_VIRTUAL)

# Test signal.siginterrupt
signal.siginterrupt(signal.SIGINT, False)
signal.siginterrupt(signal.SIGINT, True)

# Test signal.getsignal
signal.getsignal(signal.SIGINT)

# Test signal.set_wakeup_fd
signal.set_wakeup_fd(3)

# Test signal.set_wakeup_fd
signal.set_wakeup_fd(-1)

# Test signal.set_wakeup_
