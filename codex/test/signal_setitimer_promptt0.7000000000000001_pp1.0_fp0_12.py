import signal
# Test signal.setitimer()
# after setitimer() is called, the process will be sent a SIGALRM signal
# after the specified number of seconds and then at regular intervals
# after that.

# setitimer() takes three arguments: which timer to set, an interval,
# and an optional initial delay.
# The interval is specified as a tuple: (seconds, microseconds).
# The initial delay is also specified as a tuple, but it is optional.
# If omitted, the timer will start after the specified period.
# If the initial delay is specified, the timer will start after the
# initial delay, and then again after the specified period.

# If the timer is set to zero, it is disabled,
# and no further signals will be sent.

# The first argument specifies which timer is being set.
# The ITIMER_REAL timer counts down in real time, and sends SIGALRM
# when it reaches zero.
# The ITIMER_VIRTUAL timer counts down only when the process is executing,
# and sends SIGVTALRM when it reaches zero.
# The ITIMER_PROF timer counts down both when the process
