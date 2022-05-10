import signal
# Test signal.setitimer()
#
# setitimer() can be used to implement a simple timeout in Python.
# Note that this only works if the signal handler does not block.
#
# This program uses setitimer() to measure how long it takes to
# execute a piece of code.
#
# The time.time() function is used to measure the time. This is
# very simple, but not very precise. On my system, it is accurate
# to about 1/100 second.
#
# If you want to use this code in a real program, you should use
# a better timer.

# This is the function that is timed.
def timed_function(n):
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                pass

# This is the signal handler
