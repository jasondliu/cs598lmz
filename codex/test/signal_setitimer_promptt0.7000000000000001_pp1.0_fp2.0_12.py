import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)

# Test signal.getitimer
# Doesn't raise any exceptions
signal.getitimer(signal.ITIMER_VIRTUAL)

# Test signal.signal
# Raises TypeError if second argument isn't callable.
try:
    signal.signal(signal.SIGALRM, 1)
except TypeError:
    pass
else:
    print('TypeError expected')

signal.signal(signal.SIGALRM, signal.SIG_IGN)

# Test signal.getsignal
signal.getsignal(signal.SIGALRM)

# Test signal.set_wakeup_fd
signal.set_wakeup_fd(1)

# Test signal.siginterrupt
