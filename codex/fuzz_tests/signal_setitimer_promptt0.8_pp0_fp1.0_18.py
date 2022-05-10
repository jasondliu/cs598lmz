import signal
# Test signal.setitimer() for absolute timer values

import time

#
# Helper function to start timer to fire in TIMEOUT seconds
#
def setup_timer(TIMEOUT):
    # Setup signal handler
    signal.signal(signal.SIGALRM, signal_handler)

    # Set itimer to fire in TIMEOUT seconds
    signal.setitimer(signal.ITIMER_REAL, TIMEOUT, 0)

#
# Helper function to handle timer signal
#
def signal_handler(signum, frame):
    print "timeout occurred"
    sys.exit(1)

#
# Program starts here
#
TIMEOUT = 1

# Setup signal handler
signal.signal(signal.SIGALRM, signal_handler)

# Set itimer to fire in TIMEOUT seconds
signal.setitimer(signal.ITIMER_REAL, TIMEOUT, 0)

# Drain buffer fast
while 1:
    time.sleep(0.1)
    print "."
</code>
This script works perfectly fine in Python 2.5, but doesn't
