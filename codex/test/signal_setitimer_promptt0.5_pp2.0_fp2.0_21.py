import signal
# Test signal.setitimer()

# This test verifies that the SIGALRM timer can be set and that it
# is delivered to the process.

# This test is Linux and BSD specific, since it depends on the
# semantics of setitimer and the SIGALRM signal.

# This test may only be run by root, since setitimer requires
# root privileges.

# Python sets the alarm timer to 1 second during interpreter
# initialization.  If you run this test as a non-root user,
# you will get a SIGALRM before the test even starts.  If you
# run this test as root, you will not get a SIGALRM until the
# test is finished.  You can use the "time" command to see how
# long it takes to run.  If you see a SIGALRM, the test failed.

# Written by Jeff Bauer, jeffb@activestate.com

import sys
import time

