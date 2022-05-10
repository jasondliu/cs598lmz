import signal
# Test signal.setitimer() by setting a timer to go off in 1 second and
# then blocking for 2 seconds.  The timer should go off while we're
# blocked.

