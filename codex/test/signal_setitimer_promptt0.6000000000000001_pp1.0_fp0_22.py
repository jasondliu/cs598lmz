import signal
# Test signal.setitimer() with SIGPROF and SIGALRM
#
# Note, the test is not very good, as it doesn't check that SIGPROF is
# actually generated.

import sys
import time

#
# Check that SIGPROF and SIGALRM work
#

