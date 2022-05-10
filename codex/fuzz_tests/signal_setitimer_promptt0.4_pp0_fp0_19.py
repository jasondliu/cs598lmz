import signal
# Test signal.setitimer()
# setitimer() is a function that allows the process to receive a signal
# after a certain time has elapsed.
# This is useful for implementing things like timeouts.

def handler(signum, frame):
    print("Signal handler called with signal", signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)
