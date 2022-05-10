import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)
    if signum == signal.SIGALRM:
        print("SIGALRM received")
    if signum == signal.SIGVTALRM:
        print("SIGVTALRM received")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGVTALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)
signal.setitimer(signal.ITIMER_VIRTUAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

os.close(fd)
