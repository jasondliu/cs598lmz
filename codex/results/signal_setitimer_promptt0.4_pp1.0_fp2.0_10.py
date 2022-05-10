import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 1)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)

# Test signal.signal()
def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)

# Test signal.getsignal()
signal.getsignal(signal.SIGALRM)

# Test signal.pause()
signal.pause()

# Test signal.alarm()
signal.alarm(2)

# Test signal.siginterrupt()
signal.siginterrupt(signal.SIGALRM, False)

# Test signal.set_wakeup_fd()
signal.set_wakeup_fd(1)

# Test signal.set_wakeup_fd()
signal.set_wakeup_fd(2)

# Test signal.set_wakeup_fd()
signal.set
