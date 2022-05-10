import signal
# Test signal.setitimer() and signal.getitimer() with a variety of
# arguments.
#
# This test is not very thorough, it just makes sure that the
# functions don't crash.  We could add a loop to check the
# accuracy of the timers.

signal.setitimer(signal.ITIMER_REAL, 1, 2)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 2)
signal.setitimer(signal.ITIMER_PROF, 1, 2)

signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getitimer(signal.ITIMER_PROF)

# This should raise an exception
try:
    signal.setitimer(signal.ITIMER_REAL, 1)
except TypeError:
    pass
else:
    print "setitimer() didn't raise exception"

# This should raise an exception
try:
    signal.getitimer(signal
