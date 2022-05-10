import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0)
signal.setitimer(signal.ITIMER_PROF, 0)
signal.setitimer(signal.ITIMER_REAL, 0)

# Test signal.getitimer
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getitimer(signal.ITIMER_PROF)
signal.getitimer(signal.ITIMER_REAL)

# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# Test signal.alarm
signal.alarm(0)
signal.alarm(1)

# Test signal.pause
signal.pause()

# Test signal.siginterrupt
signal.sig
