import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 1, 1)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
# Test signal.signal
signal.signal(signal.SIGHUP, lambda x, y: None)
# Test signal.getsignal
signal.getsignal(signal.SIGHUP)
# Test signal.alarm
signal.alarm(1)
# Test signal.pause
signal.pause()
# Test signal.set_wakeup_fd
signal.set_wakeup_fd(1)
# Test signal.siginterrupt
signal.siginterrupt(signal.SIGALRM, False)
# Test signal.set_wakeup_fd
signal.set_wakeup_fd(1)
# Test signal.siginterrupt
signal.siginterrupt(signal.SIGALRM, False)
# Test signal.sigpending
signal.sigpending()
# Test signal.sig
