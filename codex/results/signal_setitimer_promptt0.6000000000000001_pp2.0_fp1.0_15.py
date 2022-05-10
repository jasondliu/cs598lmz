import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "Received signal", signum

# Install the signal handler and set a 1-second timer
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDONLY)

# Does not get here before timer expires and SIGALRM is sent
os.read(fd, 1000)
