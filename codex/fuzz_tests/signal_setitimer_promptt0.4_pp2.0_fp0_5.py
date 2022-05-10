import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)

# Test signal.pause()
signal.pause()

# Test signal.alarm()
signal.alarm(0)

# Test signal.getsignal()
signal.getsignal(signal.SIGALRM)
