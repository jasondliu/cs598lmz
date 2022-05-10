import signal
# Test signal.setitimer()
print('Testing setitimer()...')

def handler(signum, frame):
    print('Handler called with signal', signum)
    raise RuntimeError('this is the error message')

# Install the handler and set a 1-second timer
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)
# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDONLY)
print('Got fd', fd)
# Disable the timer
signal.setitimer(signal.ITIMER_REAL, 0)

#
# Test signal.setitimer() for an alarm
#
print('Testing setitimer() for an alarm...')

import time
from signal import alarm, signal, SIGALRM, SIGKILL
from os import kill

def set_alarm(n):
    # Call signal() with SIGALRM to set the handler to the default
    # signal handler
    signal(SIGALRM, SIG
