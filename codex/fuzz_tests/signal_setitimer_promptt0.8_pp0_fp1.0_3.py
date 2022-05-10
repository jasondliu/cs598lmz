import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Register the signal handler and define a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Read and write to the file descriptor
os.write(fd, 'Hello world\n')
print os.read(fd, 100)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)
