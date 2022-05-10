import signal
# Test signal.setitimer()

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm

# Do something with fd

os.close(fd)
