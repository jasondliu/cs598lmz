import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_VIRTUAL)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_PROF)

# Test signal.alarm()
signal.alarm(1)

# Test signal.alarm()
signal.alarm(0)

# Test signal.pause()
signal.pause()

# Test signal.set_wakeup_fd()
signal.set_wakeup
