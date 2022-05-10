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
