import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)

# Set an alarm
signal.setitimer(signal.ITIMER_REAL, 0.2)

# Do stuff
print 'Before:', signal.getitimer(signal.ITIMER_REAL)
time.sleep(0.1)
print 'After:', signal.getitimer(signal.ITIMER_REAL)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Do other stuff
time.sleep(0.3)

# Set a new alarm
signal.setitimer(signal.ITIMER_REAL, 0.2)

# Do more stuff
print 'Before:', signal.getitimer(signal.ITIMER_REAL)
time.sleep(0.1)
print 'After:', signal.getitimer(signal
