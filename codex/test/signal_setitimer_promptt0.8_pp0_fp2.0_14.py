import signal
# Test signal.setitimer() and signal.getitimer()
#
# $Id: test_signal.py,v 1.4 2001/02/27 03:18:26 fdrake Exp $

# TODO:
#
# - test SIGUSRx and SIGCLD
#   cannot test SIGCLD on MS Windows
#

import os
import sys

# Always run this test on the default signal handler
try:
    if hasattr(sys, 'setcheckinterval'):
        sys.setcheckinterval(100)
except:
    pass

# Always run this test with threads
import thread

# Modify this variable to True before running the test to enable tracing.
TRACE = False

def trace(s):
    """Trace if TRACE == True."""

    if TRACE:
        sys.stdout.write('%s\n' % s)
        sys.stdout.flush()

trace('Python version: ' + sys.version)

#
# We need to get a timeout after a while,
# but how much is "a while"? :-)
#


