import signal
# Test signal.setitimer()
#
# This test is known to fail on some systems (including FreeBSD)
# because the signal handler is not called at the expected time.
#
# The test is disabled by default.  To enable it, run this script
# with the --enable option.

import sys
import time

