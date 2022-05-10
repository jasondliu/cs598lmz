import signal
# Test signal.setitimer()
#
# The signal.setitimer() function sets the given timer to fire after the
# specified number of seconds. It returns the previous timer setting.
# The timer can be one of the following:
#   signal.ITIMER_REAL:
#     Decrement the time-of-day timer. When it reaches zero,
#     generate SIGALRM.
#   signal.ITIMER_VIRTUAL:
#     Decrement the time-of-day timer while the process is executing.
#     When it reaches zero, generate SIGVTALRM.
#   signal.ITIMER_PROF:
#     Decrement the time-of-day timer while the process is executing,
#     and while the system is running on behalf of the process.
#     When it reaches zero, generate SIGPROF.
#
# The previous timer setting is a tuple of the following form:
#   (interval, value)
#
# The interval represents the current timer setting. The value represents the
# number of timer ticks remaining until the next timer expiration.
#
# When a timer expires, the corresponding signal is sent to
