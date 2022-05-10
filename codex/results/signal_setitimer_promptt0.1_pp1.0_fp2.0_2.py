import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C to deliver a SIGINT
# Press Ctrl+\ to deliver a SIGQUIT
# Press Ctrl+Z to deliver a SIGTSTP

# The alarm signal will be delivered if the open()
# takes more than 5 seconds

# After the alarm, the signal handler raises an exception
# The exception handler opens the same device again
# and the process hangs again

# Press Ctrl+C again to deliver a SIGINT
# Press Ctrl+\ again to deliver a SIGQUIT
# Press Ctrl+Z again to deliver a SIGTSTP

# The alarm signal will be delivered if the open()
# takes more than 5 seconds

# After the
