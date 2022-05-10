import signal
# Test signal.setitimer
#
# This tests setting the ITIMER_PROF timer.  The timer is set for 1 second
# and we sleep for 1.5 seconds.  We expect to receive a SIGPROF signal.
#
# Python signal module sends SIGVTALRM on Linux instead of SIGPROF.  If
# Python is compiled with ucontext, then it sends the correct signal.
#
# Python signal module sends SIGALRM on OSX instead of SIGPROF.

import os, sys
import signal
import time

