import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.setitimer(signal.ITIMER_REAL, 0)
# Now do some work, and try not to hang...

# Read the existing data
os.read(fd, 1000)

# Truncate the file
os.ftruncate(fd, 0)

# Write some more data
os.write(fd, b'0123456789abcdef')

# Close the file
os.close(fd)
