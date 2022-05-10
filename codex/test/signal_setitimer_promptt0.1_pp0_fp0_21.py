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

# After 5 seconds, a SIGALRM signal is sent
# and the handler is called.  Then the
# alarm is reset for another 5 seconds.

# Note that SIGALRM is not an instantaneous signal;
# it may take a few seconds to be delivered.

# Press Ctrl+C again before the second alarm
# to interrupt the read() and see the handler
# called a second time.

# After the read(), the remaining alarm is canceled
# and no more SIGALRM signals are sent
