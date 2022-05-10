import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now

# This read() may hang indefinitely
os.read(fd, 1000)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Press Ctrl+C now

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# This read() may hang indefinitely
os.read(fd, 1000)
