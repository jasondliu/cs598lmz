import signal
# Test signal.setitimer() on Linux and Mac.
signal.setitimer(signal.ITIMER_REAL, 1, 1)
# Test signal.setitimer() on Windows.
signal.setitimer(signal.ITIMER_REAL, 1, 1)

# Test signal.set_wakeup_fd() on Linux.
signal.set_wakeup_fd(1)

# Test signal.signal() on Linux.
signal.signal(signal.SIGUSR1, lambda x, y: None)
signal.signal(signal.SIGUSR1, signal.SIG_DFL)
signal.signal(signal.SIGUSR1, signal.SIG_IGN)

# Test signal.siginterrupt() on Linux.
signal.siginterrupt(signal.SIGUSR1, True)
signal.siginterrupt(signal.SIGUSR1, False)

# Test signal.sigpending() on Linux.
signal.sigpending()

# Test signal.
