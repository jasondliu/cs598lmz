import signal
# Test signal.setitimer()
def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Now set another alarm
signal.setitimer(signal.ITIMER_REAL, 3)

# Disable the alarm for now
signal.setitimer(signal.ITIMER_REAL, 0)

