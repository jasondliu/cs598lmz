import signal
# Test signal.setitimer()
#
#
# $Id: setitimer.py,v 1.1 2004-02-27 21:32:51 eddy Exp $
#
# setitimer() is not implemented on all platforms.
# If not, skip this test.
try:
    signal.setitimer(signal.ITIMER_REAL, 1, 0)
except AttributeError:
    raise TestSkipped, "setitimer() not available"

# This test is not very good, because it doesn't actually test anything.
signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
signal.setitimer(signal.ITIMER_PROF, 1, 0)
