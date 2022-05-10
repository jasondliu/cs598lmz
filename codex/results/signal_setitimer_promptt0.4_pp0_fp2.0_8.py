import signal
# Test signal.setitimer and signal.getitimer

def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

os.write(fd, 'This is a test\n'.encode())

signal.setitimer(signal.ITIMER_REAL, 0)
# Disable the alarm
os.close(fd)
# fd is now closed, so the alarm signal handler will not be called
# when the timer expires

# Test signal.setitimer and signal.getitimer

def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
sign
