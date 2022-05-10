import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.setitimer(signal.ITIMER_REAL, 0)
# Read the file descriptor
os.read(fd, 1)

# Expected output:
#   Signal handler called with signal 14
#   Traceback (most recent call last):
#     File "itimer.py", line 13, in <module>
#       fd = os.open('/dev/ttyS0', os.O_RDWR)
#     File "itimer.py", line 6, in handler
#       raise OSError("Couldn't open device!")
