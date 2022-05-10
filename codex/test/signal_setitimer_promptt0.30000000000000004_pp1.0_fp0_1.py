import signal
# Test signal.setitimer
#
# This test is not very comprehensive.  It just makes sure that the
# setitimer() call doesn't crash.  It does not check that the timer
# actually fires.

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
