import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

# Test signal.siginterrupt
signal.siginterrupt(signal.SIGCHLD, True)
signal.siginterrupt(signal.SIGCHLD, False)

# Test signal.sigpending
signal.sigpending()

# Test signal.sigwait
signal.sigwait((signal.SIGINT, signal.SIGTERM))

# Test signal.sigwaitinfo
signal.sigwaitinfo((signal.SIGINT, signal.SIGTERM))

# Test signal.strsignal
signal.strsignal(signal.SIGABRT)

# Test signal.getsignal
