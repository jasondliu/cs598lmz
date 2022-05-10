import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.setitimer(signal.ITIMER_REAL, 0)
# Now do some work, and try not to hang...

# Set the signal handler back to the default handler
signal.signal(signal.SIGALRM, signal.SIG_DFL)

# Set an alarm to wake us up in 5 seconds
signal.alarm(5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Disable the alarm
signal.alarm(0)
#
