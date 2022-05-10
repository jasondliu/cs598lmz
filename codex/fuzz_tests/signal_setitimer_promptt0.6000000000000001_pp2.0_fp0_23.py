import signal
# Test signal.setitimer()
import time

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# This open() may hang indefinitely
#fd = os.open('/dev/ttyS1', os.O_RDWR)

# This open() may hang indefinitely
#fd = os.open('/dev/ttyS2', os.O_RDWR)

# This open() may hang indefinitely
#fd = os.open('/dev/ttyS3', os.O_RDWR)

# Do something else
while 1:
    time.sleep(1)
    print 'not hanging...'
