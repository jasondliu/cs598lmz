import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "Signal handler called with signal", signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C to deliver a SIGINT
# Press Ctrl+\ to deliver a SIGQUIT
# Press Ctrl+Z to deliver a SIGTSTP

# After 5 seconds, a SIGALRM signal is sent
# and the handler is called.  The alarm is
# not reset by default, so only one signal is sent.

# After the signal handler returns, the next open()
# call may hang indefinitely again.

# Press Ctrl+C again, and the open() call
# is interrupted by the SIGINT signal.

# Press Ctrl+\ again, and the open() call
# is interrupted by the SIGQUIT signal.

# Press Ctrl
