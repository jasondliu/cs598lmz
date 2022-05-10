import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Test signal.getsignal()
signal.getsignal(signal.SIGINT)

# Test signal.getsignal()
signal.getsignal(signal.SIGALRM)

# Test signal.getsignal()
signal.getsignal(signal.SIGCHLD)

# Test signal.getsignal()
signal.getsignal(signal.SIGURG)

# Test signal.getsignal()
signal.getsignal(signal.SIGWINCH)

# Test signal.getsignal()
signal.getsignal(signal.SIGIO)

# Test signal.getsignal()
signal.getsignal(signal.SIGPIPE)

# Test signal.getsignal()
signal.getsignal(signal.SIGSYS)

# Test signal.getsignal()
