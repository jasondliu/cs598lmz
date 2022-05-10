import signal
# Test signal.setitimer()
def signal_handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 5)
# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm

# do something with fd

os.close(fd)

# Test signal.setitimer()
def signal_handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 5)
# This open()
