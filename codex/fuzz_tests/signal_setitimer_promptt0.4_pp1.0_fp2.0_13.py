import signal
# Test signal.setitimer()

# The signal.setitimer() function sets the given timer to fire in the given
# number of seconds, and the timer will fire every given interval after that.
# The timer can be one of signal.ITIMER_REAL, signal.ITIMER_VIRTUAL or
# signal.ITIMER_PROF.

# The signal.getitimer() function returns the time until the timer fires.

# The signal.alarm() function is a simplified interface, where the timer is
# always signal.ITIMER_REAL, and only one timer can be used at a time.

# The signal.ITIMER_REAL timer decrements in real time, and delivers SIGALRM
# upon expiration.

# The signal.ITIMER_VIRTUAL timer decrements only when the process is
# executing, and delivers SIGVTALRM upon expiration.

# The signal.ITIMER_PROF timer decrements both when the process is executing
# and when the system is executing on behalf of the process. Coupled with
# itimer.ITIMER_VIRTUAL, this timer is usually used
