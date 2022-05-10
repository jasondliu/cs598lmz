import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C to deliver a SIGINT
signal.pause()

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

print 'Disabled the alarm'

# Press Ctrl+C again to deliver a SIGINT
signal.pause()

# Close the file descriptor
os.close(fd)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

print 'Disabled the alarm'
