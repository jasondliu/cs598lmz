import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 2)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)

# Test signal.signal()
signal.signal(signal.SIGHUP, signal.SIG_IGN)

# Test signal.getsignal()
signal.getsignal(signal.SIGHUP)

# Test signal.pause()
signal.pause()

# Test signal.alarm()
signal.alarm(5)

# Test signal.getpid()
signal.getpid()
