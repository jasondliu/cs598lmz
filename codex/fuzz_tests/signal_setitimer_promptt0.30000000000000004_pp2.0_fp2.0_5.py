import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the timer to go off in 2 seconds
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# This read() may hang indefinitely
os.read(fd, 1000)
