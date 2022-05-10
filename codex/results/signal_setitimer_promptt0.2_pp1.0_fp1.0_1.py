import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now!

# After 5 seconds, a SIGALRM signal is sent
# and the signal handler is called.  The open()
# call is interrupted, so an exception is raised.

# The exception is caught and the function exits.

# The alarm is not reset by the signal handler,
# so after another 5 seconds, SIGALRM is sent
# again and the signal handler is called again.

# The second time, the exception is not caught
# and the program is terminated.

# The alarm is now reset to 0, so no more SIGALRM
# signals are sent.
