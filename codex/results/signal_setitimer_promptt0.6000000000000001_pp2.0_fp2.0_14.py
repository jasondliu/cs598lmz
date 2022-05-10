import signal
# Test signal.setitimer()

import sys

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Itimer error")

# Set the signal handler and a 5-second interval
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttys003', os.O_RDWR)

while True:
    print('Yay!')
