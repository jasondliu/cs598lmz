import signal
# Test signal.setitimer()
#
# This test is a bit tricky.  We need to make sure that the timer
# expires at the correct time, but we can't just have the test hang
# waiting for the timer to expire.  The solution is to have the
# signal handler for the timer set a global variable, and then have
# the main thread poll that variable.
#
# This test is a bit simplistic.  It only tests that the timer fires
# within a reasonable amount of time.  It doesn't check that the
# timer fires multiple times.
#
# The test is run with both the old and new signal module.
#
# XXX: This test is not run with the -uall option.  It fails when run
# with -uall because the test is too slow.  The test takes about a
# second to run, and the -uall option sets a timeout of 0.5 seconds.
#
# Python issue #1539

import time
import sys
import os
import signal

# The time at which the test started, in seconds since the epoch.
start_time = time.time()

# The time at which the
