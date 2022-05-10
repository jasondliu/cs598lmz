import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now!

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Do something else
print 'Doing something else'

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Do something else
print 'Doing something else'

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Do something else
print 'Doing something else'

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL
