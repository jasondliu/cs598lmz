import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.2)
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.2)
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_PROF)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_VIRTUAL)
# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
# Test signal.pause
signal.pause()
# Test signal.alarm
signal.alarm(10)
# Test signal.set_wakeup_fd
signal.set_wakeup_fd(1)
# Test signal.set_wakeup_fd
signal.set_wakeup_fd(-1)
# Test signal.set
