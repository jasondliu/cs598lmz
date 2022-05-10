import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 2.0, 2.0)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_VIRTUAL)

# Test signal.alarm
signal.alarm(2)
signal.alarm(0)

# Test signal.pause
signal.pause()

# Test signal.signal
signal.signal(signal.SIGUSR1, lambda signum, frame: None)

# Test signal.getsignal
signal.getsignal(signal.SIGUSR1)

# Test signal.set_wakeup_fd
signal.set_wakeup_fd(123)

# Test signal.set_wakeup_fd
signal.set_wakeup_fd(123)

# Test signal.siginterrupt
signal.siginterrupt(signal.SIGUSR1, True)

# Test signal.sigpending
signal.sigpending()

# Test signal.
