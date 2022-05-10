import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now to send a signal

# After 5 seconds, a SIGALRM signal is sent
# and the signal handler is called.  The open()
# call is interrupted, and an IOError is raised.

# A slightly better way to do this is to use the
# signal.alarm() function, which does not require
# the use of signal.ITIMER_REAL.

# After setting the alarm, we should pause() to
# wait until the signal handler returns.  Note
# that pause() does not work on Windows.

# signal.alarm(5)
# signal.pause()

# Now continue with the rest
