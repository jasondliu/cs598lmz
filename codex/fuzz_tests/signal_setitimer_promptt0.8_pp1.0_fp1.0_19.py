import signal
# Test signal.setitimer()

# The SIGALRM signal is delivered when the timer expires.
# alarm() (without setitimer) uses SIGALRM
# on Linux, Mac OS X, FreeBSD, NetBSD and OpenBSD.

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL,5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

print('fd =', fd)

signal.setitimer(signal.ITIMER_REAL,0)
# Disable the alarm

# Do some stuff with fd

os.close(fd)
