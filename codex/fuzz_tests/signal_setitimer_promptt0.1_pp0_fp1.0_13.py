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

# After 5 seconds, a SIGALRM signal is sent
# This will wake up the open() call, and the
# signal handler will be called

# Now we can read and write the ttyS0 device
os.write(fd, 'Hello!\n')
print 'ALARM!'
os.close(fd)
