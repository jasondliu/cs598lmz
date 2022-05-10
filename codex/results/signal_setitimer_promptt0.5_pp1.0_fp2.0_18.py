import signal
# Test signal.setitimer
#
# This test checks that the setitimer() function can be called from Python
# code.  Note that the function is not tested for correctness, only for
# existence.

signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)
