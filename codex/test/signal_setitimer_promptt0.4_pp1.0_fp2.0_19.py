import signal
# Test signal.setitimer()

# This test is a bit tricky to get right, because it's not easy to
# tell if the signal handler was called at the right time.  So we
# just do a few iterations of the test, and hope we get lucky.

import signal
import time

def handler(signum, frame):
    global count
    count += 1
