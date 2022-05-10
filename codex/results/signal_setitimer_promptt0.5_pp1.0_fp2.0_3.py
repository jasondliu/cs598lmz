import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# Test signal.alarm
signal.alarm(1)
# Test signal.alarm
signal.alarm(1)
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# Test signal.siginterrupt
signal.siginterrupt(signal.SIGINT, False)
# Test signal.siginterrupt
signal.siginterrupt(signal.SIGINT, True)
# Test signal.set_wakeup_fd
signal.set_wakeup_fd(1)
# Test signal.set_wakeup_fd
signal.set_wakeup_fd(1)
#
