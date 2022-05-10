import signal
# Test signal.setitimer()
#
# This test is only valid on systems that support the setitimer() system
# call.  It is not valid on Windows.
#
# This test is intended to be run under a debugger.  It will abort if
# the debugger does not respond to the SIGALRM signal.

import os
import sys
import signal
import time

# This test is only valid on systems that support the setitimer() system
# call.  It is not valid on Windows.
if not hasattr(signal, 'setitimer'):
    sys.exit(0)

