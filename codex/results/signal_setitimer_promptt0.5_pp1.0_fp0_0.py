import signal
# Test signal.setitimer()
# The signal module defines a set of functions to deal with signals.
# The signal.setitimer() function sets the given interval timer.
# The timer is identified by which. The value of which can be one of the following:
# signal.ITIMER_REAL: Decrements in real time, and delivers SIGALRM upon expiration.
# signal.ITIMER_VIRTUAL: Decrements only when the process is executing, and delivers SIGVTALRM upon expiration.
# signal.ITIMER_PROF: Decrements both when the process is executing and when the system is executing on behalf of the process.
# Coupled with ITIMER_VIRTUAL, this timer is usually used to profile the time spent by the application in user and kernel space.
# signal.ITIMER_REAL: Decrements in real time, and delivers SIGALRM upon expiration.
# The interval timer value is specified in seconds and microseconds in the value argument.
# The current value of the timer is returned in the old_value argument as a tuple of seconds and microseconds.
# The timer remains active even after a signal handler for SIGALRM is invoked.
