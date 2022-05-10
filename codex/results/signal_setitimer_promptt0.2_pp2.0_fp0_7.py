import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# After 5 seconds, a SIGALRM signal is sent
# and the signal handler is called.  The open()
# then returns with an error.

# After the signal handler returns, the alarm
# is reset to 5 seconds in the future.

# The alarm continues to fire every 5 seconds
# until the program exits.

# Note that the handler remains in effect, so
# the alarm continues to fire even after the
# first open() has returned with an error.

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Disable the alarm
signal.setitimer
