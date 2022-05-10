import signal
# Test signal.setitimer()
#
# This program tests signal.setitimer() by setting up a SIGALRM handler
# and a SIGPROF handler.  The SIGALRM handler prints a message, and
# the SIGPROF handler increments a counter.  The test passes if the
# counter is incremented every second.

import signal

# The signal handler for SIGALRM
