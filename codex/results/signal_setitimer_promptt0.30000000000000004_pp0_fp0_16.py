import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

# This open() may hang indefinitely
fd = os.open('/dev/tty', os.O_RDWR)

# This read() may hang indefinitely too.
os.read(fd, 1)

# So may this write()
os.write(fd, '*')

# This close() may hang indefinitely too.
os.close(fd)
