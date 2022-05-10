import signal
# Test signal.setitimer() and signal.getitimer()

# ITIMER_REAL decrements in real time, and delivers SIGALRM upon expiration
signal.setitimer(signal.ITIMER_REAL, 3.2)
time.sleep(1.1)
print signal.getitimer(signal.ITIMER_REAL)
time.sleep(1.1)
print signal.getitimer(signal.ITIMER_REAL)
time.sleep(2.9)
# Alarm fires here, but there is no handler, so we get a SIG_DFL handler
print "Expected alarm here"
time.sleep(1.1)
print signal.getitimer(signal.ITIMER_REAL)

# ITIMER_REAL decrements in real time, and delivers SIGALRM upon expiration
signal.setitimer(signal.ITIMER_VIRTUAL, 3.2)
time.sleep(1.1)
print signal.getitimer(signal.ITIMER_VIRTUAL)
time.sleep(1.1)
print
