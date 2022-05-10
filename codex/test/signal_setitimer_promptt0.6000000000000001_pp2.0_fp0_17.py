import signal
# Test signal.setitimer(which, seconds, interval)
#
# The following is only valid for Unix.
#
# The timer is armed for seconds, and after each expiry, the timer is
# rearmed for interval.  If interval is zero, the timer will be disarmed
# after the first expiry.
#
# When the timer expires, a SIGALRM signal will be sent to the process.
#
# The first argument, which, may be ITIMER_REAL, ITIMER_VIRTUAL or
# ITIMER_PROF, to request timing of the indicated resource.  If the
# platform supports it, ITIMER_REAL timers will also wake up the process
# on clock ticks.  The ITIMER_VIRTUAL timer is based on the amount of
# time the process spends executing, and the ITIMER_PROF timer is based
# on the total amount of time spent executing by the process and by its
# children.
#
# This function returns the old values of the timer, as a tuple of three
# floats: (delay, interval, unused).  The unused value is always 0.0 and
#
