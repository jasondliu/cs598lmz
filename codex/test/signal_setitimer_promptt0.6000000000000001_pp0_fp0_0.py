import signal
# Test signal.setitimer()
import sys

if sys.platform == "win32":
    print("test_signal skipped on Windows")
    sys.exit(0)

import time
from test import support

# For debugging, uncomment the following line and set
# the appropriate signal number
#signum = signal.SIGUSR1

# The following is a list of timers that are
# currently running.
active = []

def handler(signum, frame):
    # print "handler called for signal", signum
    # Find out which timer caused this handler to be called.
    for timer in active[:]:
        if timer.pending():
            timer.cancel()
            active.remove(timer)

# Arrange for handler() to be called for each kind of
# timer supported by this platform.  This test is
# meant to exercise the signal module, not the timer
# mechanism, so we don't worry about how accurate the
# timers are.

if not hasattr(signal, "setitimer"):
    print("test_signal skipped -- no setitimer()")
    sys
