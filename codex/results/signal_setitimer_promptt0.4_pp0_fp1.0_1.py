import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)

# Test signal.alarm
signal.alarm(1)

# Test signal.signal
signal.signal(signal.SIGALRM, lambda x,y:None)

# Test signal.getsignal
signal.getsignal(signal.SIGALRM)

# Test signal.set_wakeup_fd
signal.set_wakeup_fd(0)

# Test signal.siginterrupt
signal.siginterrupt(signal.SIGALRM, True)

# Test signal.pause
signal.pause()

# Test signal.default_int_handler
signal.default_int_handler(signal.SIGALRM, None)

# Test signal.getsignal
signal.getsignal(signal.SIGALRM)

# Test signal.set_
