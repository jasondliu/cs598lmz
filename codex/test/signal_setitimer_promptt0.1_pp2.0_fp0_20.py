import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C to deliver a SIGINT
signal.pause()

# Flush output buffers and close the file descriptor
os.write(fd, b'G1 X0 Y0\n')
os.close(fd)

# Set the handler back to the default and set a new alarm
signal.signal(signal.SIGALRM, signal.SIG_DFL)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C to
