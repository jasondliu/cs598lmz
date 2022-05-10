import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now

# After 5 seconds, a SIGALRM signal is sent
# and the signal handler is called.  The open()
# call is interrupted, so the function returns
# an error.

# The alarm is not reset by the signal handler,
# so after another 5 seconds, the signal handler
# is called again.

# Press Ctrl+C again and the program terminates.

# This behavior can be used to time out functions
# that fail to return normally.  For example,
# urllib.urlopen() does not have a time out feature.
# But you can write a function that uses a timeout
# using signal.
