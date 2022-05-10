import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Test signal.set_wakeup_fd()
signal.set_wakeup_fd(sys.stdout.fileno())

# Test signal.getsignal()
signal.getsignal(signal.SIGALRM)

# Test signal.pause()
signal.pause()

# Test signal.set_wakeup_fd()
signal.set_wakeup_fd(-1)

# Test signal.getsignal()
signal.getsignal(-1)

# Test signal.setitimer()
signal.setitimer(-1, 0.1, 0.1)
