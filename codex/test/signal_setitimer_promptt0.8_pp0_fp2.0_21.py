import signal
# Test signal.setitimer()
#
# The alarm() function is a quick way to set a timer, but it only supports
# integer seconds, and only one timer at a time.  The setitimer() function
# is more flexible, allowing a second argument of less than one in which
# case we will get a timer that goes off after a fraction of a second.  The
# first argument of setitimer() is an integer which specifies the type of
# timer to use.  The second argument is the delay in seconds for the timer.
# The third argument is an optional repeating delay for the timer.
#
# The signal.SIGALRM constant is used to specify the 'alarm' timer.  The
# signal.SIGVTALRM constant is the 'virtual' alarm timer.  The two are
# independent - when one goes off, that does not affect the other.  Using
# signal.SIGALRM, I got a delay of approximately 1.0011 seconds on a typical
# run.  On the other hand, signal.SIGVTALRM had a delay of 0.5 seconds.
#
# setitimer(), like the the signal.sign
