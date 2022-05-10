import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C to deliver a SIGINT
# Press Ctrl+\ to deliver a SIGQUIT
# Press Ctrl+Z to deliver a SIGTSTP

# After the alarm goes off, a SIGALRM signal is sent to the process,
# and the signal handler is invoked.
# The alarm() function returns the number of seconds remaining
# before the alarm would have gone off.
# The setitimer() function returns a tuple containing the
# number of seconds and microseconds remaining before the alarm would have gone off.
# The getitimer() function returns a tuple containing the
# number of seconds and microseconds remaining before the alarm would have gone off.

#
