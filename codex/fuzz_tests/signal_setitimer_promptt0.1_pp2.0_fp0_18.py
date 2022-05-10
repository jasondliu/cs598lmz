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
# and the signal handler is called.  The open()
# call is interrupted, and an IOError is raised.

# After the signal handler returns, the alarm
# is reset to 5 more seconds.

# This works only on Unix.

# On Windows, the signal handler is always called
# after the specified time, but the open() call
# is not interrupted.

# On Windows, the signal module is not available.
