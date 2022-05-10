import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "Signal handler called with signal", signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now

# After 5 seconds, a SIGALRM signal is sent
# and the signal handler is called.  The alarm is not
# reset by default, so only one signal is sent.

# This open() may hang indefinitely again
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C again, and the signal handler is called again.

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# This open() may hang indefinitely again
fd = os.open('/dev/ttyS0', os.O_RD
