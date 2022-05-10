import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now to send a SIGINT before the alarm goes off
# Now the alarm should go off

# After the signal handler returns, the original alarm settings are restored.
# The alarm will not be reset by the signal handler.

# The following line is never executed because
# the program is terminated with the exception.
print('Continuing')
