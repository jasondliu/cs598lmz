import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 5, 0)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)

# Test signal.getsignal
signal.getsignal(signal.SIGALRM)

# Test signal.signal
signal.signal(signal.SIGALRM, signal.SIG_DFL)

# Test signal.alarm
signal.alarm(5)

# Test signal.pause
signal.pause()

# Test signal.siginterrupt
signal.siginterrupt(signal.SIGALRM, True)

# Test signal.set_wakeup_fd
signal.set_wakeup_fd(-1)

# Test signal.sigpending
signal.sigpending()

# Test signal.sigwait
signal.sigwait((signal.SIGALRM,))

# Test signal.sigwaitinfo
signal.sigwaitinfo((signal.S
