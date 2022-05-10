import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)
    raise OSError("Got expected signal")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

print("file descriptor", fd)
os.close(fd)
