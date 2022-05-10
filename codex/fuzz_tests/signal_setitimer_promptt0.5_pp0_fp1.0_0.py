import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)

# Schedule the first alarm for 1 second from now
signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)

# This open() may hang indefinitely
fd = os.open('/dev/tty', os.O_RDWR)

# Schedule the second alarm for 2 seconds from now
signal.setitimer(signal.ITIMER_REAL, 2.0, 0.0)

os.write(fd, 'About to hang...\n')

# This read() may hang indefinitely
os.read(fd, 1024)
