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
# call is interrupted, and an exception is
# raised.

# A slightly better approach is to use a try:...except:
# block around the open() call, and only try to
# open the port once.

# After the signal handler returns, the alarm
# is reset to 5 seconds.

# This will continue until the user presses Ctrl+C
# to interrupt the program.

# Note that the alarm() function is a simplification
# that sets the ITIMER_REAL timer to a
