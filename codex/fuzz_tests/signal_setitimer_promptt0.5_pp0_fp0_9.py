import signal
# Test signal.setitimer()
#
# The test is designed to check if the signal is received when
# the timer expires.
#
# The test is based on the code provided by
# http://docs.python.org/library/signal.html#example
#

import time
import signal

def signal_handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

os.write(fd, 'foo')
os.close(fd)
