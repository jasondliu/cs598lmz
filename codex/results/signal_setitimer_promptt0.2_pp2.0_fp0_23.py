import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

os.write(fd, 'Hello world\n')

# Now I can do other things here, and get a
# signal when the timer expires

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

os.write(fd, 'Hello world\n')

# Now I can do other things here, and get a
# signal when the timer expires
