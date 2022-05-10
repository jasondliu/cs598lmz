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
# Now do some work, and try not to hang...
# ...

os.close(fd)

# The following example shows how to use the alarm() function to limit
# the amount of time spent in a blocking operation.

import signal
import time

def alarm_handler(signum, frame):
    print('Alarm!')
    raise OSError("Timeout!")

signal.signal(signal.SIGALRM, alarm_handler)

signal.
