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

signal.alarm(0)          # Disable the alarm

print('Doing non-blocking read')
try:
    os.read(fd, 1)
except OSError as e:
    print('Got OSError', e)
else:
    print('read() returned')

print('Doing blocking read')
try:
    os.read(fd, 1)
except OSError as e:
    print('Got OSError', e)
else:
    print('read() returned')
