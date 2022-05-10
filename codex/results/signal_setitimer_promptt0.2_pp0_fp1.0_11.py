import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

print('Yay!')

# After 10 seconds, a SIGALRM signal is sent
# and the handler is called.  Then the alarm is reset
# for 5 more seconds.

# If the open() call returns, the alarm is canceled.

# If the open() call does not return, the alarm
# is reset and the handler is called again in 5 seconds.

# The handler will continue to be called every 5 seconds
# until the open() call returns.

# The alarm is then canceled and the program continues.

# The handler will not be called again.

# The alarm is reset to 0.0, disarming it.
signal
