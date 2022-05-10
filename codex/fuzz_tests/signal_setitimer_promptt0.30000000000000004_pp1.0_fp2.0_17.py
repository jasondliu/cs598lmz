import signal
# Test signal.setitimer()

import signal

def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL,5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C to deliver a SIGINT to the process
# The read should be interrupted by the alarm
# and the process should exit with a KeyboardInterrupt
try:
    print('Reading...')
    os.read(fd, 1024)
except KeyboardInterrupt:
    print('\nKeyboardInterrupt')
    exit(0)

# Press Ctrl+C again before the alarm
# to interrupt the read() again
# and prove that the alarm is still scheduled
try:
    print('Reading again...')
    os.read(fd, 1024)
except KeyboardInterrupt:
    print('\nKeyboardInterrupt')
