import signal
# Test signal.setitimer() and signal.getitimer().
from test import test_support, support
import unittest
import time

# Skip this test if the platform doesn't have itimer support.
support.get_attribute(signal, 'ITIMER_REAL')

# Since we need to test that the timers are not active after fork() (see
# issue1331), we need support for the subprocess module.
support.requires("subprocess")


# I had a lot of trouble trying to get reliable timing using
# threading.Timer.  Some systems seem to have a minimum timer interval;
# using threading.Timer objects with intervals less than this seemed
# to be pretty much random as to when they would actually expire.
# On some systems, this minimum interval is greater than 10 msecs.
#
# So, in the signal_timing() test below, we use alarm() and SIGALRM
# instead of threading.Timer to implement the test timing.

# On some platforms (notably OS X), SIGALRM can't be caught.  So,
# define an alternate signal to use there.
