import signal
# Test signal.setitimer
# This test is not very good, because it is not clear what the
# exact timing should be.  It is used to check that the signal
# is delivered at about the right time.

import time

