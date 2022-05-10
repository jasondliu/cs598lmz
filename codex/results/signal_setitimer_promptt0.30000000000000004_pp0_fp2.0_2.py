import signal
# Test signal.setitimer() and signal.getitimer()

# This test is only valid if the timer is implemented in terms of
# setitimer(2) and getitimer(2).  If the timer is implemented in
# another way, this test will fail.

# The test works by setting the timer to a very small value, and
# waiting for the signal to be delivered.  The signal handler sets
# a global variable, and the main program checks that the variable
# was set.

# This test is not valid if the timer is implemented in terms of
# alarm(2), since alarm(2) is reset by a signal handler.

# This test is not valid if the timer is implemented in terms of
# setitimer(2) with ITIMER_REAL, since setitimer(2) with ITIMER_REAL
# is reset by a signal handler.

# This test is not valid if the timer is implemented in terms of
# setitimer(2) with ITIMER_VIRTUAL, since the signal handler runs
# as part of the timer expiration, and the signal handler is not
# allowed to call setit
