import signal
# Test signal.setitimer
#
# This test should print "signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)"
# every second.  If it doesn't, the test fails.

